# Simple script using ipaddress module to print out useable IP range for subnet

import ipaddress 

net4 = ipaddress.ip_network('192.0.2.0/28')
for x in net4.hosts():
    print(x)

