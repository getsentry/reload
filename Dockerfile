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
RUN cp $(find /usr/lib -name 'libmaxminddb.so.0' | head -1) /usr/local/lib/libmaxminddb.so.0


FROM gcr.io/distroless/python3-debian13

# Make installed packages and libmaxminddb discoverable
ENV PYTHONPATH=/usr/local/lib/python3.13/site-packages \
    LD_LIBRARY_PATH=/usr/local/lib

# Python packages installed in the build stage
COPY --from=build /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# mywsgi console script (invoked via /usr/bin/python3 to bypass the build-stage shebang)
COPY --from=build /usr/local/bin/mywsgi /usr/local/bin/mywsgi

# libmaxminddb is not included in distroless but is needed by geoip2
COPY --from=build /usr/local/lib/libmaxminddb.so.0 /usr/local/lib/libmaxminddb.so.0

COPY reload_app /usr/src/reload/reload_app

WORKDIR /usr/src/reload

EXPOSE 8000

USER nonroot

CMD ["/usr/bin/python3", "/usr/local/bin/mywsgi", "reload_app.wsgi:application", "0.0.0.0:8000"]
