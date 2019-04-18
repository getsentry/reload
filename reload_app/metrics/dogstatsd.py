from .base import Metrics


class DogStatsdMetrics(Metrics):
    def __init__(self, id, prefix=None, tags=None, host="127.0.0.1", port=8125):
        self.id = id
        self.prefix = prefix
        self.tags = tags or {}
        self.host = host
        self.port = port
        self.tags["instance"] = id

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

    def decrement(self, metric, value=1, tags=None, sample_rate=1):
        self.client.decrement(
            self._get_key(metric),
            value,
            sample_rate=sample_rate,
            tags=self._get_tags(tags),
        )

    def histogram(self, metric, value, tags=None, sample_rate=1):
        self.client.histogram(
            self._get_key(metric),
            value,
            sample_rate=sample_rate,
            tags=self._get_tags(tags),
        )

    def timing(self, metric, value, tags=None, sample_rate=1):
        self.client.timing(
            self._get_key(metric),
            value,
            sample_rate=sample_rate,
            tags=self._get_tags(tags),
        )

    def timed(self, metric, tags=None, sample_rate=1, use_ms=None):
        self.client.timed(
            self._get_key(metric),
            sample_rate=sample_rate,
            tags=self._get_tags(tags),
            use_ms=use_ms,
        )
