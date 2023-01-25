from mininet.topo import Topo

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.node import RemoteController
import copy
import random
import sys

import time
REMOTE_CONTROLLER_IP = "127.0.0.1"
N_SERVERS = 3
N_CLIENTS = 5
N_SWITCHES = 7
bw = 0.5
class SingleTopo(Topo):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
        ser = []
        cli = []
        swi = []

        for i in range(1,N_SWITCHES+1):
            swi.append(self.addSwitch('s'+str(i)))
        

        for i in range(1,N_SERVERS+1):
            ser.append(self.addHost('h'+str(i)))
        
        for i in range(N_SERVERS+1,N_SERVERS+1+N_CLIENTS+1):
            cli.append(self.addHost('h'+str(i)))
        
        self.mh = self.addHost('h100')
        self.addLink(self.mh,swi[0])

        swi_1 = copy.deepcopy(swi)
        swi_1.pop(0)
        swi_2 = [swi[0]]

        while swi_1:
            s1 = random.choice(swi_1)
            s2 = random.choice(swi_2)
            swi_1.remove(s1)
            swi_2.append(s1)
            self.addLink(s1, s2,cls=TCLink,bw=bw)
        
        for _ in range(5):
            s1 = random.choice(swi_2)
            s2 = random.choice(swi_2)
            if s1==s2:
                continue
            self.addLink(s1, s2,cls=TCLink,bw=bw)

        self.cli = cli
        self.ser = ser

        for es in ser:
            self.addLink(es,random.choice(swi),cls=TCLink,bw=bw)
        
        for ec in cli:
            self.addLink(ec,random.choice(swi),cls=TCLink,bw=bw)
        # for c in cli:
        #     # print("Client:",net.get(c).cmd('/home/deshiyan/miniconda3/bin/python random_requests.py & sleep 0.2'))
        #     print("Client:",net.get(c).cmd('./rand_req.sh & sleep 0.2'))

topos = { 'mytopo': ( lambda: SingleTopo() ) }



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
