from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.files import write_file
from nornir import InitNornir
from nornir.core.filter import F

BACKUP_PATH = "./configs"


def backup_config(task, path):
    r = task.run(task=networking.napalm_get, getters=["config"])
    task.run(
        task=write_file,
        content=r.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )


nr = InitNornir(config_file="./config.yml")

devices = nr.filter((F(groups__contains="CSR_Routers")))

result = devices.run(
    name="Backup Device Configurations", path=BACKUP_PATH, task=backup_config
)

print_result(result, vars=["stdout"])