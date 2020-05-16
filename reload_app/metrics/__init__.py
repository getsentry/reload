VALID_METRICS = {
    ### metrics that occur inside of the React application ###
    "app.component.render": ("timing", ["name"]),
    "app.component.async-component": ("timing", ["route", "error"]),
    # TODO:
    #  'app.component.dynamic-import-fail': [],
    ### metrics related to page/script loads ###
    # time it takes to load scripts in <head>
    "app.page.head-load": ("timing", []),
    # time it takes to load everything at the end of <body>
    "app.page.body-load": ("timing", []),
    # time it takes to fetch, parse, and execute main js app
    "app.page.bundle-load": ("timing", []),
    # when the main js bundle fails to load
    "app.page.bundle-load-fail": ("increment", []),
    "app.api.discover-query": ("timing", ["status"]),
    "app.api.request-success": ("timing", ["path", "status"]),
    "app.api.request-error": ("timing", ["path", "status"]),
    "app.api.request-abort": ("increment", []),
    # used for performance measurements such as
    # when /organizations/{org_slug}/ endpoint finishes and state is refreshed
    "app.component.perf": ("timing", ["name", "route", "organization_id"]),
    # app.perf.page.<name> are metrics to measure load time for specific pages
    # - group: Control or experiment group for perf upgrades
    # - milestone: Key points in the loading of a page (e.g. First Meaningful Paint)
    # - start_type: 'cold-start' or 'warm-start' for loading a page
    "app.page.perf.issue-list": (
        "timing",
        ["org_id", "group", "start_type", "milestone", "is_enterprise", "is_outlier"],
    ),
    "app.page.perf.issue-details": (
        "timing",
        ["org_id", "group", "start_type", "milestone", "is_enterprise", "is_outlier"],
    ),
}

VALID_GLOBAL_TAGS = {"release"}
