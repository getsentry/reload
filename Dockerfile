FROM python:3.7-slim-buster

RUN groupadd -r reload && useradd -r -g reload reload

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

ENV GOSU_VERSION=1.12 \
    GOSU_SHA256=0f25a21cf64e58078057adc78f38705163c1d564a959ff30a891c31917011a54 \
    TINI_VERSION=0.19.0 \
    TINI_SHA256=93dcc18adc78c65a028a84799ecf8ad40c936fdfc5f2a57b1acda5a8117fa82c

RUN set -x \
     && fetchDeps=" \
        wget \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $fetchDeps && rm -rf /var/lib/apt/lists/* \
    # grab gosu for easy step-down from root
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \
    && echo "$GOSU_SHA256 /usr/local/bin/gosu" | sha256sum --check --status \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    # grab tini for signal processing and zombie killing
    && wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v$TINI_VERSION/tini-amd64" \
    && echo "$TINI_SHA256 /usr/local/bin/tini" | sha256sum --check --status \
    && chmod +x /usr/local/bin/tini \
    && tini -h \
    && apt-get purge -y --auto-remove $fetchDeps

RUN apt-get update && apt-get install -y --no-install-recommends \
        libmaxminddb-dev \
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
