import ipaddress;
import json;

class IPRange:
    def ip_range(self, environ, response):
        _net = str(environ['params'].get('ip'));
        _net = _net if _net is not None else '172.16.197.0/24';
        ip_range = [];
        for a in ipaddress.ip_network(_net):
            ip_range.append(str(a));
        result = json.dumps(ip_range).encode('utf-8');
        response('200 Ok', [('Content-Type', 'application/json;charset=utf-8'), ('Content-length', str(len(result)))]);
        yield result;