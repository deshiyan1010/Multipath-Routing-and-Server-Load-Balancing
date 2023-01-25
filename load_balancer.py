import sys
from flask import Flask
import random
import time
from stats import Stats
import os
import json
from load_balance_logic import LB
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import requests

app = Flask(__name__)

lb = LB()


@app.route('/compute')
def compute():
    s = lb.lb_next('cpu')
    print("Diverted to",s)
    return requests.get('http://'+s+':5000/compute').json()

@app.route('/stats')
def stats():
    s = lb.read()
    return s

if __name__ == '__main__':
    app.run(host= sys.argv[1], port=5000, debug=False,use_reloader=False)
    

## metrics
# cpu
# mem
# active_connection
# data_packets_sent
# data_packets_received
# data_bytes_sent
# data_bytes_received
# response_time