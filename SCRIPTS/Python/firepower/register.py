#!/usr/bin/python
import json
import connect
import sys

host = "fmc.dcloud.local"
username = "restapiuser"
password = "C1sco12345"
name="NGFW"

#connect to the FMC API
headers,uuid,server = connect.connect (host, username, password)

user_input = str(raw_input("Would you like to register the managed device? [y/n]
"))
if user_input == "y":
     policy_name = str(raw_input("Enter name of new Access Control Policy to be
create:"))
     access_policy = {
          "type": "AccessPolicy",
          "name": policy_name,
          "defaultAction": { "action": "BLOCK" }
          }
     post_response = connect.accesspolicyPOST(headers,uuid,server,access_policy)
     policy_id = post_response["id"]
     print "\n\nAccess Control Policy\n" + policy_name + "\ncreated\n\n"
     device_post = {
                       "name": name,
                       "hostName": "ngfw.dcloud.local",
                       "regKey": "C1sco12345",
                       "type": "Device",
                       "license_caps": [
                         "BASE",
                         "MALWARE",
                         "URLFilter",
                         "THREAT"
                       ],
                       "accessPolicy": {
                         "id": policy_id,
                         "type": "AccessPolicy"
                       }
                     }
     post_data = json.dumps(device_post)

     output =  connect.devicePOST (headers, uuid, server, post_data)
#    print "\n\nPost request is: \n" + json.dumps(output,indent=4) + "\n\n"

# GET ALL THE DEVICES AND THEIR corresponding interfaces

user_input = str(raw_input("In the FMC UI, confirm that the device discovery has completed and then press 'y' to continue or '
n' to exit. [y/n]"))
headers,uuid,server = connect.connect (host, username, password)
if user_input == "n":
  quit()

devices = connect.deviceGET(headers,uuid,server)
for device in devices["items"]:
  if  device["name"] == name:
    print "DEVICE FOUND, setting ID"
    device_id = device["id"]

# NOW THAT WE HAVE THE DEVICE ID WE NEED TO GET ALL THE INTERFACES

interfaces = connect.interfaceGET(headers,uuid,server,device_id)
# Interfaces i want to change
interface_1 = "GigabitEthernet0/0"
interface_2 = "GigabitEthernet0/1"

for interface in interfaces["items"]:
  if interface["name"] == interface_1:
    interface_1_id = interface["id"]
    print "interface 1 found"
  if interface["name"] == interface_2:
    interface_2_id = interface["id"]
    print "interface 2 found"

user_input = str(raw_input("Would you like to configure device interfaces? [y/n]"))

if user_input == "y":
     interface_put = {
                             "type": "PhysicalInterface",
                             "hardware": {
                               "duplex": "AUTO",
                               "speed": "AUTO"
                             },
                             "enabled": True,
                             "MTU": 1500,
                             "managementOnly": False,
                             "ifname": "outside",
                             "enableAntiSpoofing": False,
                             "name": "GigabitEthernet0/0",
                             "id": interface_1_id,
                             "ipv4" : {
                              "static": {
                                "address":"https://protect-eu.mimecast.com/s/DY5pC0g0RiMW3RriwawTw?domain=198.18.133.2",
                                "netmask":"18"
                              }
                             }
                           }
     put_data = json.dumps(interface_put)
     connect.interfacePUT (headers, uuid, server, put_data,device_id,interface_1_id)
     interface_put = {
                             "type": "PhysicalInterface",
                             "hardware": {
                               "duplex": "AUTO",
                               "speed": "AUTO"
                             },
                             "enabled": True,
                             "MTU": 1500,
                             "managementOnly": False,
                             "ifname": "inside",
                             "enableAntiSpoofing": False,
                             "name": "GigabitEthernet0/1",
                             "id": interface_2_id,
                             "ipv4" : {
                              "static": {
                                "address":"https://protect-eu.mimecast.com/s/s5EhCg5nJimW2LYHoUcxo?domain=198.19.10.1",
                                "netmask":"24"
                              }
                             }
                           }
     put_data = json.dumps(interface_put)
     connect.interfacePUT (headers, uuid, server, put_data,device_id,interface_2_id)
[root@inside bin]#
