#!/usr/bin/env python3

# Example code to get output from Cisco ASA

import getpass 
import re 
import sys

from netmiko import ConnectHandler

net_device_username = ('roger')
net_device_password = ('cisco')
# Set enable/secret = password for now
net_device_secret = net_device_password

# Setup a dict with our ASAvs in it, in real world this could be read
# from a CSV or the CLI or any other source
firewalls = {
    "ASAv-1": {"ip": "192.168.1.245", "platform": "cisco_asa"},
    "ASAv-2": {"ip": "192.168.1.246", "platform": "cisco_asa"},
}
 
# Setup an empty dict for our results:
results = {}
 
# Instantiate netmiko connection objects and gather the output of
# `show version | inc So|Serial| up' on these two firewalls
for fw_name, fw_data in firewalls.items():
    print(f"Connecting to {fw_name}...")
    fw_connection = ConnectHandler(
        ip=fw_data["ip"],
        device_type=fw_data["platform"],
        username=net_device_username,
        password=net_device_password,
        secret=net_device_secret,
    )
    results[fw_name] = fw_connection.send_command(
        command_string="show version | inc So|Serial| up"
    )
 
# Print our results
for fw_name, result in results.items():
    print(f"{fw_name} information:\n")
    print(result)
 
sys.exit()