#!/bin/bash

set -e

if [ "${1:0:1}" = '-' ]; then
    set -- granian "$@"
fi

# Write credentials JSON to disk for google.auth to pick it up
if [ -n "$GOOGLE_APPLICATION_CREDENTIALS_JSON" ]; then
    tmp=$(mktemp)
    echo "$GOOGLE_APPLICATION_CREDENTIALS_JSON" > $tmp
    unset GOOGLE_APPLICATION_CREDENTIALS_JSON
    export GOOGLE_APPLICATION_CREDENTIALS=$tmp
fi

exec "$@"
