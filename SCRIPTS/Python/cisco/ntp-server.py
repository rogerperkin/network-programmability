from netmiko import ConnectHandler

devices = '''
CSR-1
CSR-2
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'roger'
password = 'cisco'
verbose = True
ntp_commands = ['ntp server 4.4.4.4' , 'ntp server 5.5.5.5']

for device in devices:
        print(" Connecting to Device: " + device)
        net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)

        prompter = net_connect.find_prompt()
        if '>' in prompter:
                net_connect.enable()

        output = net_connect.send_command('show run | inc ntp')
        
        if not 'ntp server' in output:
            print('NO NTP servers are configured on device: ' + device)
            answer = input('Would you like you enable NTP on: ' + device + ' <y/n> ')
            if answer == 'y':
                output = net_connect.send_config_set(ntp_commands)
                print(output)
                print('NTP is now configured!')
                print('Better save the config!')
                output = net_connect.send_command('wr mem')
                print('Config saved on ' + device)
            else:
                print('No NTP configurations have been made!')

        else:
            print("NTP is already configured on device: " + device)