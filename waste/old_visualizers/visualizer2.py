import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import json
import os

from topo import N_SERVERS


figure, axis = plt.subplots(2, 2)
axis[0,0].set_title("CPU Usage")
axis[0,1].set_title("Memory Usage")
axis[1,0].set_title("Active Connections")
server = ['10.0.0.'+str(i) for i in range(1,N_SERVERS+1)]
server.append('127.0.0.1')
server.pop(0)
cpu_usage = [0 for i in range(N_SERVERS)]
memory_usage = [0 for i in range(N_SERVERS)]
connections = [0 for i in range(N_SERVERS)]
def animate(i):
    
    index = 0

    for s in server:
        print(s)
        try:
            with open("metrics/"+s+'.json',"r") as f:
                data = json.load(f)
            cpu_usage[index] = data['cpu']
            memory_usage[index] = data['mem']
            connections[index] = data['active_connection']
        except:
            pass
        index+=1

    print(server,cpu_usage,memory_usage,connections)

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

ani = animation.FuncAnimation(figure, animate, interval=100)
plt.show()
