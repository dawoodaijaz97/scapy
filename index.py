import sys
from scapy.all import *

p = (IP(src="35.202.52.252",dst="35.193.17.254")/UDP(sport="12345",dport="12345"))/Raw(load="google")

send(p)
