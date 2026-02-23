FROM python:3.11-slim-bookworm

RUN groupadd -r reload && useradd -r -g reload reload

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

RUN apt-get update && apt-get install -y --no-install-recommends \
        libexpat1 libmaxminddb-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/reload
WORKDIR /usr/src/reload

COPY requirements.txt /usr/src/reload

RUN set -ex \
    \
    && buildDeps=' \
        gcc \
        libc6-dev \
    ' \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
    \
    && pip install --no-cache-dir -r requirements.txt \
    \
    && apt-get purge -y --auto-remove $buildDeps

COPY reload_app /usr/src/reload/reload_app
COPY docker-entrypoint.sh /usr/src/reload

EXPOSE 8000

ENTRYPOINT ["/usr/src/reload/docker-entrypoint.sh"]
CMD [ "mywsgi", "reload_app.wsgi:application", "0.0.0.0:8000" ]
