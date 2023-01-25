import os
import psutil
import time
import netifaces as ni
import psutil
pid = os. getpid()
print(pid)
# os.system('sudo cpulimit -l 50 -p '+str(pid))
# print("Done")
a = []

while 1:
    # print("Python", end='@')
    # cpu = float(os.popen('ps -p {} -o %cpu | tail -n 1'.format(pid)).read().replace('\n', '').strip())
    # mem = float(os.popen('ps -p {} -o %mem | tail -n 1'.format(pid)).read().replace('\n', '').strip())
    # print("CPU: {}\nMEM: {}".format(cpu,mem))
    # print(os.popen('ifconfig wlo1 | grep "RX packets"').read().split())
    # _,_,packets_rx,_,bytes_rx,_,_ = os.popen('ifconfig wlo1 | grep "RX packets"').read().split()
    # _,_,packets_tx,_,bytes_tx,_,_ = os.popen('ifconfig wlo1 | grep "TX packets"').read().split()
    # packets_rx = float(packets_rx)
    # packets_tx = float(packets_tx)
    # bytes_rx = float(bytes_rx)
    # bytes_tx = float(bytes_tx)

    a.append(0)
    # break
    # if(len(a)%1000000==0):
    #     print('\r{}'.format(len(a)),end='')
    # time.sleep(0.2)