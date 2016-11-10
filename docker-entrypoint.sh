#!/bin/bash

set -e

if [ "${1:0:1}" = '-' ]; then
    set -- uwsgi "$@"
fi


if [ "$1" = 'uwsgi' -a "$(id -u)" = '0' ]; then
    # uwsgi options that must exist
    export UWSGI_MASTER=true
    export UWSGI_WSGI_FILE=app.py
    export UWSGI_CALLABLE=app
    export UWSGI_DIE_ON_TERM=true
    export UWSGI_ENABLE_THREADS=true

    set -- gosu reload tini -- "$@"
fi

exec "$@"
