from pendu_var import *
from colors import bcolors
import os
import platform

def clear_all():
    os.system(f'cmd /c {os_cmd[os_cmd.index(platform.system()) + 1]}')

def lettre_devi_fc(letter, word):
    try:
        word.index(letter)
        return True
    except:
        return False

def update_interface(word, custom, string, no_letter, hangphase):
    clear_all()
    lettre_devi_str = ""
    no_letter_str = ""
    for i in lettre_devi:
        lettre_devi_str = f"{i} {lettre_devi_str}"
    for i in no_letter:
        no_letter_str = f"{no_letter_str} {i}"
    print(f"Lettre(s) en trop: {lettre_devi_str}")
    print(separator)
    print(hang[hangphase])
    print(separator)
    print(f"Le mot: {no_letter_str}")
    print(separator)
    if custom:
        test_letter = input(string)
    else:
        test_letter = input(">> Tester une lettre: ")
    return test_letter