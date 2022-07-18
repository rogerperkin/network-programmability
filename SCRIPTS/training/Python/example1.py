# Use Netmiko to connect to Cisco using SSH and run simple commands 
#!/usr/bin/python

from netmiko import ConnectHandler

CSR = {
    'device_type': 'cisco_ios',
    'ip': 'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345'
}

net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show ip int brief')
print (output)

# Finally close the connection
net_connect.disconnect()