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

def ask_replay(word, hangphase, no_letter, colors, function):
    replay = input(f"{colors}Voulez-vous rejouer ? [1] Oui [2] Non:{bcolors.ENDC}")
    if replay.isdigit():
        replay = int(replay)
        if replay < 1:
            if function == "win":
                return win(word, hangphase, no_letter)
            else:
                return game_over(word, hangphase, no_letter)
        elif replay > 2:
            if function == "win":
                return win(word, hangphase, no_letter)
            else:
                return game_over(word, hangphase, no_letter)
        elif replay == 1:
            return True
        elif replay == 2:
            return False
    else:
        if function == "win":
            return win(word, hangphase, no_letter)
        else:
            return game_over(word, hangphase, no_letter)

def game_over(word, hangphase, no_letter):
    clear_all()
    lettre_devi_str = ""
    word_str = ""
    for i in word:
        word_str = f"{word_str}{i}"
    print(f"{bcolors.FAIL}VOUS AVEZ PERDU !{bcolors.ENDC}")
    print(separator)
    print(f"{bcolors.FAIL}{hang[hangphase]}{bcolors.ENDC}")
    print(separator)
    print(f"{bcolors.FAIL}Le mot était: {word_str}{bcolors.ENDC}")
    print(separator)
    return ask_replay(word, hangphase, no_letter, bcolors.FAIL, "game_over")

def win(word, hangphase, no_letter):
    clear_all()
    lettre_devi_str = ""
    word_str = ""
    for i in word:
        word_str = f"{word_str}{i}"
    print(f"{bcolors.OKGREEN}VOUS AVEZ GAGNÉ !{bcolors.ENDC}")
    print(separator)
    print(f"{bcolors.OKGREEN}{hang[hangphase]}{bcolors.ENDC}")
    print(separator)
    print(f"{bcolors.OKGREEN}Le mot était: {word_str}{bcolors.ENDC}")
    print(separator)
    return ask_replay(word, hangphase, no_letter, bcolors.OKGREEN, "win")