import requests
import time
import random
from topo import N_SERVERS


while 1:
    time.sleep(1)
    s = random.randint(1,N_SERVERS)
    try:
        requests.get('http://10.0.0.{}:5000/compute'.format(s))
    except:
        print("failed")
    print(s)