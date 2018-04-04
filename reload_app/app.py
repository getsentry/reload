import os
import time

from base64 import b64encode
from datetime import datetime
from google.cloud import pubsub_v1
from json import load, dumps
from raven.middleware import Sentry
from werkzeug.wrappers import Response
from uuid import uuid1

from .raven_client import client
from .router import Router
from .worker import BigQueryWorker
from .utils import format_datetime, ip_from_request

COMMON_FIELDS = ('url', 'referrer', 'title', 'path', 'search', 'anonymous_id', 'user_id')

# Poor man's validation.
VALID_EVENTS = {
    'assistant.search': {
        'query': str,
    },
    'assistant.guide_cued': {
        'guide': int,
        'cue': str,
    },
    'assistant.guide_opened': {
        'guide': int,
    },
    'assistant.guide_dismissed': {
        'guide': int,
        'step': int,
    },
    'assistant.guide_finished': {
        'guide': int,
        'useful': bool,
    },
    'issue.search': {
        'query': str,
    },
}

# Prefix event names to avoid collisions with events from Sentry backend.
EVENT_NAME_TEMPLATE = 'reload.%s'


def validate_user_id(uid):
    if uid not in (None, 'undefined'):
        try:
            int(uid)
        except ValueError:
            client.captureException()
            return False
    return True


class App(Router):
    routes = {
        '/page/': 'page_view',
        '/event/': 'event',
    }

    def __init__(self, dataset, table, pubsub_project, pubsub_topic):
        super(App, self).__init__()

        self.worker = BigQueryWorker(dataset, table, flush_interval=1)

        batch_settings = pubsub_v1.types.BatchSettings(
            max_bytes=1024*1024*5,
            max_latency=0.05,
            max_messages=1000,
        )
        self.publisher = pubsub_v1.PublisherClient(batch_settings)
        self.topic = self.publisher.topic_path(pubsub_project, pubsub_topic)

    # TODO(adhiraj): Put pageviews in the events table.
    def page_view(self, request):
        # Make sure we only get POST requests
        if request.method != 'POST':
            return Response('method not allowed\n', status=405)

        start = datetime.utcnow()

        try:
            data = load(request.stream)
        except Exception:
            return Response('bad request\n', status=400)

        row = {
            'id': uuid1().hex,
            'received_at': format_datetime(start),
            'context': {
                'ip': ip_from_request(request),
                'user_agent': request.environ.get('HTTP_USER_AGENT'),
            },
        }

        try:
            row['sent_at'] = format_datetime(
                datetime.utcfromtimestamp(int(data['sent_at']) / 1000)
            )
        except Exception:
            # I dunno, maybe KeyError or it's not an integer
            row['sent_at'] = row['received_at']

        for field in COMMON_FIELDS:
            if field == 'user_id' and not validate_user_id(data.get(field)):
                return Response('bad request\n', status=400)
            try:
                row[field] = data[field]
            except KeyError:
                pass

        self.worker.queue(row)
        return Response(status=201, headers=(
            ('Access-Control-Allow-Origin', '*'),
        ))

    def event(self, request):
        # Make sure we only get POST requests
        if request.method != 'POST':
            return Response('method not allowed\n', status=405)

        start = datetime.utcnow()

        try:
            data = load(request.stream)
        except Exception:
            return Response('bad request\n', status=400)

        if data.get('event_name') not in VALID_EVENTS:
            return Response('bad request\n', status=400)

        clean_data = {
            'received_at': format_datetime(start),
            'context': {
                'ip': ip_from_request(request),
                'user_agent': request.environ.get('HTTP_USER_AGENT'),
            },
        }
        try:
            clean_data['sent_at'] = format_datetime(
                datetime.utcfromtimestamp(int(data['sent_at']) / 1000)
            )
        except Exception:
            # I dunno, maybe KeyError or it's not an integer
            clean_data['sent_at'] = clean_data['received_at']

        for field in COMMON_FIELDS:
            if field == 'user_id' and not validate_user_id(data.get(field)):
                return Response('bad request\n', status=400)
            try:
                clean_data[field] = data[field]
            except KeyError:
                pass

        for field, typ in VALID_EVENTS[data['event_name']].items():
            if field not in data:
                continue
            try:
                typ(data[field])
            except ValueError:
                client.captureException()
                return Response('bad request\n', status=400)
            clean_data[field] = data[field]

        # Conforms to super-big-data.analytics.events schema.
        row = {
            'uuid': b64encode(uuid1().bytes),
            'timestamp': time.time(),
            'type': EVENT_NAME_TEMPLATE % data['event_name'],
            'data': clean_data,
        }
        self.publisher.publish(self.topic, data=dumps(row))

        return Response(status=201, headers=(
            ('Access-Control-Allow-Origin', '*'),
        ))


def make_app_from_environ():
    app = App(
        dataset=os.environ.get('BIGQUERY_DATASET', 'reload'),
        table=os.environ.get('BIGQUERY_TABLE', 'page'),
        pubsub_project=os.environ.get('PUBSUB_PROJECT', 'internal-sentry'),
        pubsub_topic=os.environ.get('PUBSUB_TOPIC', 'analytics-events'),
    )
    return Sentry(app, client)