# Use Netmiko to connect to Cisco using SSH and run simple commands 
#!/usr/bin/python

from netmiko import ConnectHandler
from termcolor import colored

CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'roger',
    'password': 'cisco'
}

net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('show ip int brief')
print (colored(output, "white"))

config_commands = ['interface loopback 2', 'ip address 2.2.2.2 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (colored(output, "red"))

