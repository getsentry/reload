#!/bin/bash

set -e

if [ "${1:0:1}" = '-' ]; then
    set -- uwsgi "$@"
fi

# Write credentials JSON to disk for google.auth to pick it up
if [ -n "$GOOGLE_APPLICATION_CREDENTIALS_JSON" ]; then
    tmp=$(mktemp)
    echo "$GOOGLE_APPLICATION_CREDENTIALS_JSON" > $tmp
    unset GOOGLE_APPLICATION_CREDENTIALS_JSON
    chown reload:reload $tmp
    export GOOGLE_APPLICATION_CREDENTIALS=$tmp
fi


if [ "$1" = 'uwsgi' -a "$(id -u)" = '0' ]; then
    export UWSGI_HTTP=:${PORT}

    set -- gosu reload tini -- "$@"
fi

exec "$@"
