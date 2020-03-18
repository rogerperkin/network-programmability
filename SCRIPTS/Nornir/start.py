from nornir import InitNornir

nr = InitNornir("config.yml")

from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

result = nr.run(netmiko_send_command, command_string="sh ver")

print_result(result)