# Use Netmiko to connect to Cisco using SSH and run simple commands 
#!/usr/bin/python

from netmiko import ConnectHandler

CSR = {
    'device_type': 'cisco_ios',
    'ip': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345'
}

net_connect = ConnectHandler(**CSR)
output = net_connect.send_command('sh ip int brief')
print (output)

#Discover the hostname from the prompt 
 
hostname = net_connect.send_command('show run | i hostname')
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)
 
filename = './output/' + device + '.txt'
# save backup in same folder as script use below line and comment out above line 
# filename = device + '.txt'
 
showrun = net_connect.send_command('show run')
showver = net_connect.send_command('show ver')
f = open(filename, "a")   # in append mode
f.write(showrun)
f.write("\n")
f.write(showver)
f.write("\n")
 
# Finally close the connection
net_connect.disconnect()

