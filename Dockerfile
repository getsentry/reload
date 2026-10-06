FROM us-docker.pkg.dev/sentryio/dhi-mirror/python:3.13-debian13-dev AS build

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /usr/src/reload
COPY requirements.txt .
RUN python3 -m venv /opt/venv && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


FROM us-docker.pkg.dev/sentryio/dhi-mirror/python:3.13-debian13

# Python packages installed in the build stage
COPY --from=build /opt/venv /opt/venv

COPY reload_app /usr/src/reload/reload_app

WORKDIR /usr/src/reload

EXPOSE 8000

USER nonroot

CMD ["/opt/venv/bin/granian", "--interface", "wsgi", "--host", "0.0.0.0", "--port", "8000", "reload_app.wsgi:application"]
