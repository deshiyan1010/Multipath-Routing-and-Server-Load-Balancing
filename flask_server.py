import sys
from flask import Flask
import random
import time
from stats import Stats
import os
import json
from werkzeug.serving import BaseWSGIServer

active_connection = 0
app = Flask(__name__)
s=None
stat = Stats(os. getpid(), 30, 200)
pid = os.getpid()
@app.route('/')
def hello_world():
    return 'a'


@app.route('/compute')
def compute():
    global active_connection
    active_connection+=1
    a = 1
    t = time.time()
    while time.time()-t<0.2:
        a = a*5
    del a
    active_connection-=1
    return {'response':'success','provider':sys.argv[1]}


def usage_stats():
    bandwidth = stat.network_stat()
    return {'pid':pid,'cpu':stat.cpu_stat(),'mem':stat.memory_stat(),'active_connection':active_connection,'data_packets_sent':bandwidth['tx']['packets'],'data_packets_received':bandwidth['rx']['packets'],'data_bytes_sent':bandwidth['tx']['bytes'],'data_bytes_received':bandwidth['rx']['bytes']}

@app.route('/usage_stats')
def write_stats():
    return usage_stats()

if __name__ == '__main__':
    app.run(host= sys.argv[1], port=5000, debug=False,use_reloader=False)
    


