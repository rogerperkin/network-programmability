from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir import InitNornir
from nornir.core.filter import F

BACKUP_PATH = "~network-programmability/SCRIPTS/Nornir/configs"

nr = InitNornir(config_file="./config.yml")

def backup_config(task, path):
    r = task.run(task=napalm_get, getters=["config"])
    task.run(
        task=write_file,
        content=r.result["config"]["running"],
        filename=f"{path}/{task.host}.txt",
    )

devices = nr.filter(F(groups__contains="CSR"))

result = devices.run(
    name="Backup Device Configurations", path=BACKUP_PATH, task=backup_config
)

print_result(result, vars=["stdout"])