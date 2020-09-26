import shutil
import os

path = os.getcwd()
print(shutil.disk_usage(path))
print(os.system("df -h"))


