import cgi;

def notFound(environ, response):
    result = 'Not Found'.encode('utf-8');
    response('404 Not Found', [('Content-Type', 'text/plain'), ('Content-length', str(len(result)))]);
    yield result;

class PathDispatcher:
    def __init__(self):
        self.pathmap = {};
    def __call__(self, environ, response):
        path = environ['PATH_INFO'];
        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ);
        method = environ['REQUEST_METHOD'].lower();
        environ['params'] = { key: params.getvalue(key) for key in params};
        handler = self.pathmap.get((method, path), notFound);
        return handler(environ, response);
    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function;
        return function;
