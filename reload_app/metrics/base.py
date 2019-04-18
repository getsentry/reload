class Metrics(object):
    def __init__(self, id, prefix=None, tags=None):
        self.id = id
        self.prefix = prefix
        self.tags = tags or {}

    def setup(self):
        pass

    def _get_key(self, key):
        if self.prefix:
            return ".".join((self.prefix, key))
        return key

    def _get_tags(self, tags=None):
        if tags is None:
            tags = {}
        if self.tags:
            tags.update(self.tags)
        if not tags:
            return None
        return [f"{key}:{value}" for key, value in tags.items()]

    def gauge(self, metric, value, tags=None, sample_rate=1):
        pass

    def increment(self, metric, value=1, tags=None, sample_rate=1):
        pass

    def decrement(self, metric, value=1, tags=None, sample_rate=1):
        pass

    def histogram(self, metric, value, tags=None, sample_rate=1):
        pass

    def timing(self, metric, value, tags=None, sample_rate=1):
        pass

    def timed(self, metric, tags=None, sample_rate=1, use_ms=None):
        pass
