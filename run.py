#!/usr/bin/env python

import os
from werkzeug.serving import run_simple
from reload_app.app import make_app_from_environ

port = int(os.environ.get("PORT", 8000))

run_simple(
    "127.0.0.1",
    port,
    make_app_from_environ(),
    use_debugger=True,
    use_reloader=True,
    static_files={"/client": "client"},
)
