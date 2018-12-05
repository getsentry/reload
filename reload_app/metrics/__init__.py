VALID_METRICS = {
    ### metrics that occur inside of the React application ###
    'app.component.render': ('timing', ['name'],),

    # TODO:
    #  'app.component.api': [],
    #  'app.component.dynamic-import-fail': [],

    ### metrics related to page/script loads ###

    # time it takes to load scripts in <head>
    'app.page.head-load': (
        'timing',
        [],
    ),

    # time it takes to load everything at the end of <body>
    'app.page.body-load': (
        'timing',
        [],
    ),

    # time it takes to fetch, parse, and execute main js app
    'app.page.bundle-load': ('timing', []),

    # when the main js bundle fails to load
    'app.page.bundle-load-fail': ('increment', []),

    'app.api.request-success': ('timing', ['path', 'status']),
    'app.api.request-error': ('timing', ['path', 'status']),
    'app.api.request-abort': ('increment', []),
}

VALID_GLOBAL_TAGS = [
    'release',
]
