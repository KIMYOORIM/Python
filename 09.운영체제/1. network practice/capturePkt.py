from scapy.all import *

def pkt_callback(pkt):
    pkt.show() # debug statement

sniff(iface="ens3f0", prn = lambda x: x.summary(), filter="tcp", store=0)
#sniff(iface="ens3f0", prn = lambda x: x.show(), filter="tcp", store=0)
