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
#output = net_connect.send_command('show version')
#print (output)

#Discover the hostname from the prompt 
 
hostname = net_connect.send_command('show run | i hostname')
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)
 
filename = '/home/roger/network-programmability/SCRIPTS/training/Python/' + device + '.txt'
# save backup in same folder as script use below line and comment out above line 
# filename = device + '.txt'
 
showrun = net_connect.send_command('show run')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")   # in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
 
# Finally close the connection
net_connect.disconnect()