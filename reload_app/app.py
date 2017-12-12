import os
import time

from datetime import datetime
from google.cloud import pubsub_v1
from json import load
from werkzeug.wrappers import Response
from uuid import uuid1

from .router import Router
from .worker import BigQueryWorker
from .utils import format_datetime, ip_from_request

NULLABLE_FIELDS = (
    'url', 'referrer', 'title', 'path', 'search',
    'anonymous_id', 'user_id',
)
VALID_EVENT_NAMES = ('click', )

# Prefix event names to avoid collisions with events from Sentry backend.
EVENT_NAME_TEMPLATE = 'reload.%s'

BQ_PROJECT = 'internal-sentry'
BQ_TOPIC = 'analytics-events'

class App(Router):
    routes = {
        '/page/': 'page_view',
        '/event/': 'event',
    }

    def __init__(self, dataset, table, publisher, topic):
        super(App, self).__init__()
        self.worker = BigQueryWorker(dataset, table, flush_interval=1)
        self.publisher = publisher
        self.topic = topic

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

        for field in NULLABLE_FIELDS:
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

        if data.get('event_name') not in VALID_EVENT_NAMES:
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

        for field in NULLABLE_FIELDS:
            try:
                clean_data[field] = data[field]
            except KeyError:
                pass

        row = {
            'uuid': uuid1().hex,
            'timestamp': time.time(),
            'type': EVENT_NAME_TEMPLATE % data['event_name'],
            'data': clean_data,
        }
        self.publisher.publish(self.topic, data=row)

        return Response(status=201, headers=(
            ('Access-Control-Allow-Origin', '*'),
        ))


def make_app_from_environ():
    settings = pubsub_v1.types.BatchSettings(
        max_bytes=1024 * 1024 * 5,
        max_latency=0.05,
        max_messages=1000,
    )
    publisher = pubsub_v1.PublisherClient(settings)
    topic = publisher.topic_path(BQ_PROJECT, BQ_TOPIC)

    return App(
        dataset=os.environ.get('BIGQUERY_DATASET', 'reload'),
        table=os.environ.get('BIGQUERY_TABLE', 'page'),
        publisher=publisher,
        topic=topic,
    )
