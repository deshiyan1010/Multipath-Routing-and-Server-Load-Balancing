import json
import os
from topo import N_SERVERS
import requests
import time

server = ['10.0.0.'+str(i) for i in range(1,N_SERVERS+1)]
class LB:
    def __init__(self):
        self.agg_data = {}
        self.last_read = 0
        
    def read(self):
        if time.time()-self.last_read>0.3:
            for s in server:
                t = time.time()
                response = requests.get('http://'+s+':5000/usage_stats')
                resp_time = time.time()-t
                data = response.json()
                data['response_time'] = resp_time
                self.agg_data[s] = data 
            self.last_read = time.time()

        return self.agg_data

    def lb_next(self,metric='cpu'):
        data = self.read()
        minServer = None 
        minMetric = float('inf')
        for k,v in data.items():
            if v[metric]<minMetric:
                minServer = k 
                minMetric = v[metric]
            print(k,v[metric])
        return minServer

