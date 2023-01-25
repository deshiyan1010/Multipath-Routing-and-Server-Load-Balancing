from mininet.topo import Topo

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

from mininet.node import RemoteController

import sys

import time
REMOTE_CONTROLLER_IP = "127.0.0.1"
N_SERVERS = 5
N_CLIENTS = 40


class SingleTopo(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
        s = []
        c = []
        switch = self.addSwitch('s1')

        for i in range(1,N_SERVERS+1):
            s.append(self.addHost('h'+str(i)))
        
        for i in range(N_SERVERS+1,N_SERVERS+1+N_CLIENTS+1):
            c.append(self.addHost('h'+str(i)))
        
        self.mh = self.addHost('h'+str(N_SERVERS+N_CLIENTS+10))
        self.addLink(self.mh,switch)


        self.c = c
        self.s = s

        for es in s:
            self.addLink(es,switch)
        
        for ec in c:
            self.addLink(ec,switch)


if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleTopo()
    net = Mininet(topo=topo,
                  controller=None,
                  autoStaticArp=True)
    net.addController("c0",
                      controller=RemoteController,
                      ip=REMOTE_CONTROLLER_IP,
                      port=6653)
    # net.build()
    net.start()
    print("Running app on servers......")
    # time.sleep(3)


    i = 1
    for s in topo.s:
        # print(s,net.get(s))
        # out = net.get(s).cmd('sudo systemd-run --scope -p MemoryLimit=200M -p CPUQuota=10% ./run.sh 10.0.0.{} 10 200 &'.format(i))
        i+=1
        # print("Server",out)

    # out = net.get('h'+str(N_SERVERS+N_CLIENTS+10)).cmd('/home/deshiyan/miniconda3/bin/python monitoring_switch.py &')
    # print("MH",out)
    time.sleep(0)
    print("Running clients")
    for c in topo.c:
        # print("Client:",net.get(c).cmd('/home/deshiyan/miniconda3/bin/python random_requests.py & sleep 0.2'))
        print("Client:",net.get(c).cmd('./rand_req.sh & sleep 0.2'))
    
    print("Done..........")
    o = CLI(net)
    net.stop()




# from mininet.topo import Topo

# class MyTopo( Topo ):


#     def build( self ):
#         s = []
#         h = []

#         for i in range(1,5):
#             h.append(self.addHost('h'+str(i)))
        
#         for i in range(1,10):
#             s.append(self.addSwitch('s'+str(i)))

#         self.addLink(s[0],s[1])
#         self.addLink(s[1],s[2])
#         self.addLink(s[2],s[3])
#         self.addLink(s[0],s[5])
#         self.addLink(s[5],s[6])
#         self.addLink(s[6],s[7])
#         self.addLink(s[7],s[2])
#         self.addLink(s[5],s[8])
#         self.addLink(s[8],s[6])
#         self.addLink(s[6],s[4])
#         self.addLink(s[4],s[3])

#         self.addLink(h[0],s[0])
#         self.addLink(h[1],s[0])
#         self.addLink(h[2],s[4])
#         self.addLink(h[3],s[2])



# topos = { 'mytopo': ( lambda: MyTopo() ) }
