VALID_METRICS = {
    ### metrics that occur inside of the React application ###
    'app.component.render': [
       # component name
       'name'
    ],
    # TODO:
    #  'app.component.api': [],
    #  'app.component.dynamic-import-fail': [],

    ### metrics related to page/script loads ###

    # time it takes to load scripts in <head>
    'app.page.head-load': [],

    # time it takes to load everything at the end of <body>
    'app.page.body-load': [],

    # time it takes to fetch, parse, and execute main js app
    'app.page.bundle-load': [],

    # when the main js bundle fails to load
    'app.page.bundle-load-fail': [],
}

VALID_METRIC_TYPES = set(['increment', 'gauge'])
