FROM python:3.7-slim-buster

RUN groupadd -r reload && useradd -r -g reload reload

ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

# grab gosu for easy step-down from root
# grab tini for signal processing and zombie killing
RUN set -x \
    && export GOSU_VERSION=1.11 \
    && export TINI_VERSION=0.18.0 \
    \
     && fetchDeps=" \
        dirmngr \
        gnupg \
        wget \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $fetchDeps && rm -rf /var/lib/apt/lists/* \
    \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
    && export GNUPGHOME="$(mktemp -d)" \
     && for key in \
      B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    ; do \
      gpg --batch --keyserver hkps://mattrobenolt-keyserver.global.ssl.fastly.net:443 --recv-keys "$key" ; \
    done \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    \
    && wget -O /usr/local/bin/tini "https://github.com/krallin/tini/releases/download/v$TINI_VERSION/tini" \
    && wget -O /usr/local/bin/tini.asc "https://github.com/krallin/tini/releases/download/v$TINI_VERSION/tini.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && for key in \
      595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \
    ; do \
      gpg --batch --keyserver hkps://mattrobenolt-keyserver.global.ssl.fastly.net:443 --recv-keys "$key" ; \
    done \
    && gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \
    && gpgconf --kill all \
    && rm /usr/local/bin/tini.asc \
    && chmod +x /usr/local/bin/tini \
    && tini -h \
    \
    && rm -r "$GNUPGHOME" \
    && apt-get purge -y --auto-remove wget

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
