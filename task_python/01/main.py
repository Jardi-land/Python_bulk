"""
Homework Calculator

author: Lorenzo De Zen
"""

import os
import platform
from colors import Bcolors

os_cmd = ["Windows", "cls", "macOS", "clear", "Linux", "clear"]

def clear_all():
    """
    Desc:
        This is used to clear the console.
    """
    os.system(f"{os_cmd[os_cmd.index(platform.system()) + 1]}")

def calc(a_calc):
    """
    Desc:
        This is used to add two and then multiply it by two (arg. 1).

    Args:
        a_calc ([int]): The number we will modify.
    """
    b_calc = a_calc + 2
    c_calc = b_calc * 2
    print(c_calc)

def ask_number():
    """
    Desc:
        This is used to ask the number to modify and check it
    """
    a_calc = input("Ton nombre: ")
    if not a_calc.isdigit():
        clear_all()
        print(f"{Bcolors.FAIL}Merci de mettre un nombre !{Bcolors.ENDC}")
        ask_number()
    else:
        calc(int(a_calc))

clear_all()
ask_number()
