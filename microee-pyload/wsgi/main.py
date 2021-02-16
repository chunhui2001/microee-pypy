from wsgi.resty import PathDispatcher;
from wsgiref.simple_server import make_server;

from wsgi.IPDiscover import IPRange

### curl -i -v http://localhost:17110/ip_ranged
### https://docs.pylonsproject.org/projects/pyramid-cookbook/en/latest/testing/testing_post_curl.html
### https://www.tutorialspoint.com/python/python_cgi_programming.htm
if __name__ == '__main__':
    # Create the dispatcher and registry functions
    dispatcher = PathDispatcher();
    dispatcher.register('GET', '/ip_range', IPRange().ip_range);
    # Launch a basic server
    httpd = make_server('0.0.0.0', 8080, dispatcher);
    print('Serving on port 8080...');
    httpd.serve_forever();