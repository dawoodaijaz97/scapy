import sys
from scapy.all import *

p = (IP(src="35.202.52.252",dst="35.193.17.254")/UDP(sport=80,dport=1234))/Raw(load="google")

send(p,count=2000)

resp = sr1(p,verbose=0,timeout=10,count=20)

print(resp)


