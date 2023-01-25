import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import json
import os
import requests
from topo import N_SERVERS


figure, axis = plt.subplots(2, 2)

server = ['10.0.0.'+str(i) for i in range(1,N_SERVERS+1)]


cpu_usage = [0 for i in range(N_SERVERS)]
memory_usage = [0 for i in range(N_SERVERS)]
connections = [0 for i in range(N_SERVERS)]



def animate(i):    
    index = 0
    time.sleep(0.2)
    for s in server:
        try:
            response = requests.get('http://'+s+':5000/usage_stats')
            data = response.json()
            cpu_usage[index] = data['cpu']
            memory_usage[index] = data['mem']
            connections[index] = data['active_connection']
        except Exception as e:
            print(e)
        index+=1


    axis[0,0].set_title("CPU Usage")
    axis[0,1].set_title("Memory Usage")
    axis[1,0].set_title("Active Connections")
    axis[0,0].clear()
    axis[0,0].bar(server, cpu_usage, color ='maroon',
        width = 0.4)
    axis[0,1].clear()
    axis[0,1].bar(server, memory_usage, color ='blue',
        width = 0.4)
    axis[1,0].clear()
    axis[1,0].bar(server, connections, color ='purple',
        width = 0.4)

ani = animation.FuncAnimation(figure, animate, interval=0)
plt.show()
