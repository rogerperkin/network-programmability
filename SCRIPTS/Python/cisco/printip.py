import ipaddress 

net4 = ipaddress.ip_network('192.0.2.0/29')
for x in net4.hosts():
    print(x)