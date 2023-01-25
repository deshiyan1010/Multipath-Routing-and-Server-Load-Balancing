import os
import psutil
import time
class Stats:
    def __init__(self,pid,max_cpu,max_memory):
        self.pid = pid
        print(pid)
        self.max_memory = max_memory/float(psutil.virtual_memory()[0])*1000000*100
        self.max_cpu = max_cpu

    def pop_till_root(self,arr):
        while(arr[0]!='root'):
            arr.pop(0)
        return arr

    def cpu_stat(self):
        stat = os.popen('top -p {} -n 1 |grep {}'.format(self.pid,self.pid)).read().replace('\x1b','').split()
        stat = self.pop_till_root(stat)
        cpu = float(stat[7])/8
        return cpu
        # return cpu/self.max_cpu*100
    
    def memory_stat(self):
        stat = os.popen('top -p {} -n 1 |grep {}'.format(self.pid,self.pid)).read().replace('\x1b','').split()
        stat = self.pop_till_root(stat)
        mem = float(stat[8])
        return mem
        # return mem/self.max_memory*100

    def network_stat(self):
        packets_rx = packets_tx = bytes_rx = bytes_tx = 0

        for interface in os.listdir('/sys/class/net/'):
            _,_,packets_rx_d,_,bytes_rx_d,_,_ = os.popen('ifconfig {} | grep "RX packets"'.format(interface)).read().split()
            _,_,packets_tx_d,_,bytes_tx_d,_,_ = os.popen('ifconfig {} | grep "TX packets"'.format(interface)).read().split()
            packets_rx += float(packets_rx_d)
            packets_tx += float(packets_tx_d)
            bytes_rx += float(bytes_rx_d)
            bytes_tx += float(bytes_tx_d)

        return {'tx':{'packets':packets_tx,'bytes':bytes_tx},'rx':{'packets':packets_rx,'bytes':bytes_rx}}


if __name__=="__main__":
    s = Stats(304594, 100, 6000)
    t = time.time()
    s.cpu_stat()
    print(time.time()-t)
    t = time.time()
    s.memory_stat()
    print(time.time()-t)
    t = time.time()
    s.network_stat()
    print(time.time()-t)