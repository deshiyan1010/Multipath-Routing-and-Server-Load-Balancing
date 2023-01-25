import requests
from topo import N_SERVERS
import time
import json

metrics = {}

while 1:
    t = time.localtime()
    print(time.strftime("%H:%M:%S", t))
    # time.sleep(2)
    try:
        for i in range(1,N_SERVERS+1):
            response = requests.get('http://10.0.0.'+str(i)+':5000/usage_stats')
            j = response.json()
            metrics['10.0.0.'+str(i)] = j
        t = time.localtime()
        metrics['timestamp'] = time.strftime("%H:%M:%S", t)
        with open('metrics.json', 'w') as f:
            json.dump(metrics,f,indent=4)
    except:
        pass
    
