#!/usr/bin/env python3

import netmiko 
import yaml 

def read_yaml(path='inventory.yml'):
    with open(path) as file: 
       yaml_content = yaml.full_load(file.read())
    return yaml_content

def main():
    print(read_yaml())


COMMANDS_LIST = [
    'show clock'
    'show version'
    'show inventory'
    'show ip interface brief'
]



def collect_outputs(devices, commands):
    """

    Args: 
      devices (dict): dictionary, where key is the hostname, value is netmiko connection dictionary 
      commands (list): list of commands to be executed on every device 

    Returns: 
      dict: key is the hostname, value is string with all outputs 
    """

    for device in devices: 
        hostname = device.pop('hostname')

if __name__ == '__main__':
    main()



        