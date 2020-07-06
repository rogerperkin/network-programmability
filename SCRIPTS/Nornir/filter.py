from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="config.yml")

asas = nr.filter((F(name__contains="ASAv-1")))

result = asas.run(netmiko_send_command, command_string="show version | inc So|Serial| up")

print_result(result)