from json import load
from uuid import uuid1

from datetime import datetime
from werkzeug.wrappers import Response
from .router import Router
from .worker import BigQueryWorker
from .utils import format_datetime, ip_from_request


NULLABLE_FIELDS = (
    'url', 'referrer', 'title', 'path', 'search',
    'anonymous_id', 'user_id',
)

CONTEXT_CAMPAIGN_FIELDS = ('source', 'term', 'medium', 'content')


class App(Router):
    routes = {
        '/page/': 'page_view',
    }

    def __init__(self, dataset, table):
        super(App, self).__init__()
        self.worker = BigQueryWorker(dataset, table, flush_interval=1)

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

        campaign = {}
        for field in CONTEXT_CAMPAIGN_FIELDS:
            try:
                campaign[field] = data['context_campaign_' + field]
            except KeyError:
                pass

        if campaign:
            row['context']['campaign'] = campaign

        self.worker.queue(row)
        return Response(status=201)


def make_app_from_environ():
    import os
    return App(
        dataset=os.environ.get('BIGQUERY_DATASET', 'reload'),
        table=os.environ.get('BIGQUERY_TABLE', 'page'),
    )
