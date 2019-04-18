from werkzeug.wrappers import Request, Response


class Router(object):
    routes = {}

    def __init__(self):
        # Validate and resolve our routes
        self.actions = {}
        for k, v in self.routes.items():
            try:
                self.actions[k] = getattr(self, v)
            except AttributeError:
                raise Exception("bad route: %s" % k)

    def __call__(self, environ, start_response):
        request = Request(environ)
        try:
            view = self.actions[request.path]
        except KeyError:
            response = Response("page not found\n", status=404)
        else:
            response = view(request)
        return response(environ, start_response)
