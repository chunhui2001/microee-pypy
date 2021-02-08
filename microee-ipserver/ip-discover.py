import ipaddress;
import json;

### 计算ip地址范围
def ip_range(environ, response):
    response('200 Ok', [('Content-Type', 'application/json;charset=utf-8')]);
    _net = str(environ['params'].get('ip'));
    _net = _net if _net is not None else '172.16.197.0/24';
    ip_range = [];
    for a in ipaddress.ip_network(_net):
        ip_range.append(str(a));
    yield json.dumps(ip_range).encode('utf-8');

### https://www.tutorialspoint.com/python/python_cgi_programming.htm
if __name__ == '__main__':
    from resty import PathDispatcher;
    from wsgiref.simple_server import make_server;
    # Create the dispatcher and registry functions
    dispatcher = PathDispatcher();
    dispatcher.register('GET', '/ip_range', ip_range);
    # Launch a basic server
    httpd = make_server('', 8080, dispatcher);
    print('Serving on port 8080...');
    httpd.serve_forever();