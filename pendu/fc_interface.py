from pendu_var import *
import os
import platform

def clear_all():
    os.system(f'cmd /c {os_cmd[os_cmd.index(platform.system()) + 1]}')

def lettre_devi_fc(letter):
    lettre_devi.append(letter)
    update_interface

def update_interface(word, custom, string):
    clear_all()
    lettre_devi_str = ""
    for i in lettre_devi:
        lettre_devi_str = f"{i} {lettre_devi_str}"
    print(f"Lettre(s) en trop: {lettre_devi_str}{no_letter * (9 - len(lettre_devi))}")
    print(separator)
    print(hang[hangphase])
    print(separator)
    print(f"Le mot: {no_letter * len(word)}")
    print(separator)
    if custom:
        test_letter = input(string)
    else:
        test_letter = input(">> Tester une lettre: ")
    return test_letter