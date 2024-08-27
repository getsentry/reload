import os
import re
import time
import sentry_sdk
import logging

from base64 import b64encode
from datetime import datetime
from geoip2.errors import AddressNotFoundError
from google.cloud import pubsub_v1
from json import load, dumps
from werkzeug.wrappers import Response
from ua_parser import user_agent_parser
from uuid import uuid1

from .metrics import VALID_METRICS, VALID_GLOBAL_TAGS
from .metrics.dogstatsd import DogStatsdMetrics
from .router import Router
from .worker import BigQueryWorker
from .utils import format_datetime, ip_from_request
from .geo import geo_by_addr

sentry_sdk.init()

logger = logging.getLogger(__name__)

COMMON_FIELDS = (
    "url",
    "referrer",
    "document_referrer",
    "title",
    "path",
    "search",
    "anonymous_id",
    "user_id",
)

# Prefix event names to avoid collisions with events from Sentry backend.
EVENT_NAME_TEMPLATE = "reload.%s"

URL_FILTER_REGEX = r"(https?://)?(localhost|dev\.getsentry\.net)"

# 8k bytes is enough to fit every event if we trim certain extra large fields
MAX_PAYLOAD_SIZE = 8_000


def ok_response():
    return Response(status=201, headers=(("Access-Control-Allow-Origin", "*"),))


def error_response(text, status):
    return Response(
        text, status=status, headers=(("Access-Control-Allow-Origin", "*"),)
    )


def validate_user_id(uid):
    if uid not in (None, "undefined"):
        try:
            int(uid)
        except ValueError:
            sentry_sdk.capture_exception()
            return False
    return True


class App(Router):
    # fmt: off
    routes = {
        "/page/": "page_view",
        "/event/": "event",
        "/metric/": "metric",
        "/healthz": "healthz",
    }
    # fmt: on

    def __init__(
        self,
        dataset,
        table,
        pubsub_project,
        pubsub_topic,
        datadog_prefix,
        datadog_host,
        datadog_port,
    ):
        super().__init__()

        self.worker = BigQueryWorker(dataset, table, flush_interval=1)

        batch_settings = pubsub_v1.types.BatchSettings(
            max_bytes=1024 * 1024 * 5, max_latency=0.05, max_messages=1000
        )
        self.publisher = pubsub_v1.PublisherClient(batch_settings)
        self.topic = self.publisher.topic_path(pubsub_project, pubsub_topic)
        self.datadog_client = DogStatsdMetrics(
            datadog_prefix, prefix=datadog_prefix, host=datadog_host, port=datadog_port
        )
        self.datadog_client.setup()

    # TODO(adhiraj): Put pageviews in the events table.
    # TODO(adhiraj): This really needs a refactoring.
    def page_view(self, request):
        # Make sure we only get POST requests
        if request.method != "POST":
            return error_response("method not allowed\n", status=405)

        start = datetime.utcnow()

        try:
            data = load(request.stream)
        except Exception:
            return error_response("bad request expecting json\n", status=400)

        row = {
            "id": uuid1().hex,
            "received_at": format_datetime(start),
            "context": {
                "ip": ip_from_request(request),
                "user_agent": request.environ.get("HTTP_USER_AGENT"),
            },
        }

        try:
            row["sent_at"] = format_datetime(
                datetime.utcfromtimestamp(int(data["sent_at"]) / 1000)
            )
        except Exception:
            # I dunno, maybe KeyError or it's not an integer
            row["sent_at"] = row["received_at"]

        for field in COMMON_FIELDS:
            if field == "user_id" and not validate_user_id(data.get(field)):
                return error_response("bad request user id not valid\n", status=400)
            if field == "url" and re.match(URL_FILTER_REGEX, data.get(field, "")):
                return ok_response()
            try:
                row[field] = data[field]
            except KeyError:
                pass

        self.worker.queue(row)

        return ok_response()

    def event(self, request):
        # Make sure we only get POST requests
        if request.method != "POST":
            return error_response("method not allowed\n", status=405)

        start = datetime.utcnow()

        # validate payload size and send to Sentry
        if request.content_length > MAX_PAYLOAD_SIZE:
            message = f"event exceeds max payload size of {MAX_PAYLOAD_SIZE}\n"
            sentry_sdk.capture_message(message)
            return error_response(message, status=400)

        try:
            data = load(request.stream)
        except Exception:
            return error_response(
                f"bad request expecting json under {MAX_PAYLOAD_SIZE}\n", status=400
            )

        # pop off allow_no_schema since we don't want to pass it
        data.pop("allow_no_schema", None)
        clean_data = {
            "received_at": format_datetime(start),
            "context": {
                "ip": ip_from_request(request),
                "user_agent": request.environ.get("HTTP_USER_AGENT"),
            },
        }
        try:
            clean_data["sent_at"] = format_datetime(
                datetime.utcfromtimestamp(int(data["sent_at"]) / 1000)
            )
        except Exception:
            # I dunno, maybe KeyError or it's not an integer
            clean_data["sent_at"] = clean_data["received_at"]

        for field in COMMON_FIELDS:
            if field == "user_id" and not validate_user_id(data.get(field)):
                return error_response("bad request user id not valid\n", status=400)
            if field == "url" and re.match(URL_FILTER_REGEX, data.get(field, "")):
                return ok_response()
            try:
                clean_data[field] = data[field]
            except KeyError:
                pass

        # every schema-less event needs a user_id or organization_id
        if not data.get("user_id") and not data.get("organization_id"):
            return error_response(
                "bad request no user_id or organization_id", status=400
            )

        # blindly pass fields from the API to the event
        clean_data.update(data)

        # Conforms to super-big-data.analytics.events schema.
        row = {
            "uuid": b64encode(uuid1().bytes).decode("utf8"),
            "timestamp": time.time(),
            "type": EVENT_NAME_TEMPLATE % data["event_name"],
            "data": clean_data,
        }
        self.publisher.publish(self.topic, data=dumps(row).encode("utf8"))

        return ok_response()

    def track_single_metric(self, data, request):
        metric_name = data.get("metric_name")
        tags = data.get("tags", {})

        # allowed list of metric names
        if metric_name not in VALID_METRICS:
            return f"{metric_name}: bad request check if valid metric name"

        (metric_type, valid_tags) = VALID_METRICS[metric_name]

        # validate tags
        for tag in tags.keys():
            if tag not in valid_tags and tag not in VALID_GLOBAL_TAGS:
                return f"{metric_name}: bad request check if valid tag name"

        try:
            value = data["value"]
        except KeyError:
            # Allow default value for increment only
            if metric_type == "increment":
                value = 1
            else:
                return f"{metric_name}: bad request check if valid value for metric"

        # attach geo data
        try:
            geo = geo_by_addr(ip_from_request(request))
            if geo is not None:
                tags["country_code"] = geo.country.iso_code
            else:
                tags["country_code"] = "unknown"
        except AddressNotFoundError:
            tags["country_code"] = "unknown"
        except Exception:
            tags["country_code"] = "error"
            sentry_sdk.capture_exception()

        # attach UA data (browser)
        try:
            ua = user_agent_parser.Parse(request.environ.get("HTTP_USER_AGENT", ""))
            tags["browser"] = ua["user_agent"]["family"]
            tags["os"] = ua["os"]["family"]
        except Exception:
            tags["browser"] = "error"
            tags["os"] = "error"
            sentry_sdk.capture_exception()

        try:
            getattr(self.datadog_client, metric_type)(metric_name, value, tags=tags)
        except Exception:
            return f"{metric_name}: failed request to metrics server"

        return None

    def metric(self, request):
        # Make sure we only get POST requests
        if request.method != "POST":
            return error_response("method not allowed\n", status=405)

        try:
            data = load(request.stream)
        except Exception:
            return error_response("bad request expecting json\n", status=400)

        metric_objects = data if isinstance(data, list) else [data]

        errors = []
        for metric_object in metric_objects:
            error = self.track_single_metric(metric_object, request)
            if error is not None:
                errors.append(error)

        if errors:
            return error_response("\n".join(errors), status=400)

        return ok_response()

    def healthz(self, request):
        return Response("ok", status=200)


def make_app_from_environ():
    from werkzeug.middleware.proxy_fix import ProxyFix
    from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware

    app = App(
        dataset=os.environ.get("BIGQUERY_DATASET", "reload"),
        table=os.environ.get("BIGQUERY_TABLE", "page"),
        pubsub_project=os.environ.get("PUBSUB_PROJECT", "internal-sentry"),
        pubsub_topic=os.environ.get("PUBSUB_TOPIC", "analytics-events"),
        datadog_prefix=os.environ.get("DATADOG_PREFIX", ""),
        datadog_host=os.environ.get("DATADOG_HOST", "127.0.0.1"),
        datadog_port=int(os.environ.get("DATADOG_PORT", 8125)),
    )
    return ProxyFix(SentryWsgiMiddleware(app))
