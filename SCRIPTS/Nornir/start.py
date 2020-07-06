from nornir import InitNornir

nr = InitNornir("config.yml")

from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

devices = nr.filter (groups="CSR-Router")
result = devices.run(netmiko_send_command, command_string="sh int ip brief")

print_result(result)