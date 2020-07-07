from nornir import InitNornir
from nornir.core.filter import F

nr = InitNornir("config.yml")

from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

devices = nr.filter((F(hostname__contains="220")))

result = devices.run(netmiko_send_command, command_string="sh ip int brief")

print_result(result)
