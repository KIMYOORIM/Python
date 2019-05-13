from scapy.all import *
import sys

destIP="192.168.110.117"

def myPortScan(port):
    print("%d port scanning" % port)
    # sr1(IP(dst=destIP)/TCP(dport=port, flag="S"))
    a=report_ports(destIP,port)
    print(a)
    print(type(a))
    if "open" in a:
        print("%d port is open." % port)
        file.write("%d port is open\n" % port)
        file.write("%s" % a)
        file.write("\n")


#report_ports("192.168.110.117",[22,25])
#sr1(IP(dst="192.168.110.117")/TCP(dport=(22,25), flags="S"))   
#sr1(IP(dst="192.168.110.117")/TCP(dport=[22,25], flags="S"))   

file = open("result.txt","w") 
 
file.write("START PORT SCANNING") 
#myPortScan(22)
for i in range(1,66535):
    myPortScan(i)

