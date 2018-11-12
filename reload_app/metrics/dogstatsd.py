from .base import Metrics


class DogStatsdMetrics(Metrics):
    def __init__(self, id, prefix=None, tags=None, host='127.0.0.1', port=8125):
        self.id = id
        self.prefix = prefix
        self.tags = tags or {}
        self.host = host
        self.port = port
        self.tags['instance'] = id

    def setup(self):
        from datadog.dogstatsd import DogStatsd
        self.client = DogStatsd(host=self.host, port=self.port)

    def gauge(self, metric, value, tags=None, sample_rate=1):
        self.client.gauge(
            self._get_key(metric),
            value,
            sample_rate=sample_rate,
            tags=self._get_tags(tags),
        )

    def increment(self, metric, value=1, tags=None, sample_rate=1):
        self.client.increment(
            self._get_key(metric),
            value,
            sample_rate=sample_rate,
            tags=self._get_tags(tags),
        )
