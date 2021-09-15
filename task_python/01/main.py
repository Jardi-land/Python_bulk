from colors import bcolors
import os
import platform

os_cmd = ["Windows", "cls", "macOS", "clear", "Linux", "clear"]

def clear_all():
    os.system(f"{os_cmd[os_cmd.index(platform.system()) + 1]}")

def ask_number():
    a = input("Ton nombre: ")
    if not a.isdigit():
        clear_all()
        print(f"{bcolors.FAIL}Merci de mettre un nombre !{bcolors.ENDC}")
        ask_number()
    else:
        calc(int(a))

clear_all()
ask_number()