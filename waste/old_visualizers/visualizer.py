import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import json


figure, axis = plt.subplots(2, 2)
axis[0,0].set_title("CPU Usage")
axis[0,1].set_title("Memory Usage")
axis[1,0].set_title("Active Connections")

def animate(i):
    data = json.load(open("metrics.json","r"))
    server = []
    cpu_usage = []
    memory_usage = []
    connections = []
    for k,v in data.items():
        if(k[:3]=="10."):
            server.append(k)
            cpu_usage.append(v['cpu'])
            memory_usage.append(v['mem'])
            connections.append(v['active_connection'])

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
