from flask import Flask
from flask import request, render_template

from multiping import multi_ping, MultiPing
from ping_config import ADDRS_DICT as addrs_dict
from ping_config import REFRESH_TIME, SYSTEM_PING_COMMAND
import subprocess

app = Flask(__name__)


def add_headers_http(refresh, req, redirect=''):
    if redirect == '':
        redirect = req.url
    return {'Content-type': 'text/html; charset=utf-8', 'Refresh': '{}; url={}'.format(refresh, redirect)}


class BusStation:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.status = False


@app.route('/')
def hello_world():
    addrs = [addrs_dict[x] for x in addrs_dict]
#    responses, no_response = multi_ping(addrs, timeout=0.9, retry=2, ignore_lookup_errors=True)
    mp = MultiPing(addrs)
    mp.send()
    responses, no_response = mp.receive(0.9)
    for i in no_response:
        cmd = SYSTEM_PING_COMMAND[:]
        cmd.append(i)
        try:
            if subprocess.check_output(cmd):
                responses[i] = float(1)
        except Exception:
            pass
    res = []
    for k, v in addrs_dict.items():
        current = BusStation(k, v)
        if v in responses:
            current.status = True
        res.append(current)
    print(no_response)
    res.sort(key=lambda x: x.ip)
    # return str(res)
    return render_template('base.html', content_arr=res), 200, add_headers_http(REFRESH_TIME, request, redirect='')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5070)
