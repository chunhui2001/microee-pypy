from wsgiref.simple_server import make_server;

from wsgi.IPDiscover import IPRange
from wsgi.kline import KLine
from wsgi.resty import PathDispatcher;

### curl -i -v http://localhost:17110/ip_ranged
### https://docs.pylonsproject.org/projects/pyramid-cookbook/en/latest/testing/testing_post_curl.html
### https://www.tutorialspoint.com/python/python_cgi_programming.htm
if __name__ == '__main__':
    # Create the dispatcher and registry functions
    dispatcher = PathDispatcher();
    dispatcher.register('GET', '/ip_range', IPRange().ip_range);
    dispatcher.register('GET', '/kline', KLine().plt);
    # Launch a basic server
    httpd = make_server('0.0.0.0', 8080, dispatcher);
    print('Serving on port 8080...');
    httpd.serve_forever();