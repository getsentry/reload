FROM python:3.13-slim-trixie AS build

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc libc6-dev libmaxminddb-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/reload
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Normalize libmaxminddb.so.0 to an arch-independent path for the COPY below
RUN cp $(find /usr/lib -name 'libmaxminddb.so.0' | head -1) /tmp/libmaxminddb.so.0


FROM us-docker.pkg.dev/sentryio/dhi/python:3.13-debian13

# Restore OS metadata stripped by distroless so vulnerability scanners can identify the OS
COPY --from=build /etc/os-release /etc/os-release
COPY --from=build /var/lib/dpkg/status /var/lib/dpkg/status

# Python packages installed in the build stage
COPY --from=build /usr/local/lib/python3.13/site-packages /opt/python/lib/python3.13/site-packages

# mywsgi console script
COPY --from=build /usr/local/bin/mywsgi /opt/python/bin/mywsgi

# libmaxminddb is not bundled in the base image but is needed by geoip2
COPY --from=build /tmp/libmaxminddb.so.0 /opt/python/lib/libmaxminddb.so.0

COPY reload_app /usr/src/reload/reload_app

WORKDIR /usr/src/reload

EXPOSE 8000

USER nonroot

CMD ["/opt/python/bin/python3", "/opt/python/bin/mywsgi", "reload_app.wsgi:application", "0.0.0.0:8000"]
