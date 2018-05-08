class Router:
    def __init__(self):
        self.routes = {}

    def route(self, uri, methods):
        def register_route(handler):
            for method in methods:
                self.routes[(method, uri)] = handler

            return handler
        return register_route

    def handle_route(self, request):
        handler = self.routes[(request.method, request.uri)]
        response = handler(request)
        return f"HTTP/1.1 200 OK\r\n\r\n{response}"