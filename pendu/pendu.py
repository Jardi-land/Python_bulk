from colors import bcolors
from pendu_var import os_cmd
import os
import platform

def clear_all(my_os):
    os.system(f'cmd /c {os_cmd.my_os}')

def ask_os():
    my_os = platform.system()
    print(os_cmd.my_os)

def has_numbers(string):
    return any(char.isdigit() for char in string)

def word_check(word):
    if has_numbers(word):
        os.system('cmd /c "cls"')
        print(f"{bcolors.FAIL} Merci de ne pas mettre de nombre dans le mot{bcolors.ENDC}")
        ask_word()
    else:
        print("Non")


def ask_word():
    word = input(">> Quelle mot voulez vous faire deviner: ")
    word_check(word)

ask_os()

