from colors import bcolors
import os
import platform

os_cmd = ["Windows", "cls", "macOS", "clear", "Linux", "clear"]

def clear_all():
    os.system(f"{os_cmd[os_cmd.index(platform.system()) + 1]}")

clear_all()
