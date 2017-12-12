import json
from unittest import TestCase
from mock import patch, Mock
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse

from .app import make_app_from_environ

class AppTests(TestCase):
    @patch('google.cloud.pubsub_v1.PublisherClient')
    @patch('reload_app.app.BigQueryWorker')
    def test(self, worker_cls, publish_cls):
        mock_worker = worker_cls.return_value = Mock()
        mock_publisher = publish_cls.return_value = Mock()

        app = make_app_from_environ()
        c = Client(app, BaseResponse)
        sent_data = {
            'url': '/url/',
            'referrer': '/referrer/',
            'user_id': 1,
        }

        # /page/ endpoint.
        resp = c.post('/page/', data=json.dumps(sent_data))
        assert resp.status_code == 201
        assert mock_worker.queue.call_count == 1
        row = mock_worker.queue.call_args[0][0]
        for key in sent_data.keys() + ['id', 'received_at', 'context', 'sent_at']:
            assert key in row

        # /events/ endpoint.
        sent_data['event_name'] = 'click'
        resp = c.post('/event/', data=json.dumps(sent_data))
        assert resp.status_code == 201
        assert mock_publisher.publish.call_count == 1
        row = mock_publisher.publish.call_args[1]['data']
        for key in ('uuid', 'timestamp', 'type', 'data'):
            assert key in row
        data = row['data']
        for key in sent_data.keys() + ['received_at', 'context', 'sent_at']:
            if key != 'event_name':
                assert key in data
