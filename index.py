import sys
from scapy.all import *

p = (IP(src="10.128.0.4",dst="35.193.17.254")/UDP(sport=80,dport=1234))/Raw(load="google")

send(p,count=20000)



