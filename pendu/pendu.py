from colors import bcolors
from pendu_var import *
from fc_interface import *

hangphase = 0

def has_numbers(string):
    return any(char.isdigit() for char in string)

def is_only_letter(test_letter, word):
    clear_all()
    if len(test_letter) < 1:
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci d'indiquer une lettre: {bcolors.ENDC}")
    elif has_numbers(test_letter):
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une lettre et non un nombre: {bcolors.ENDC}")
    elif len(test_letter) > 1:
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une seule lettre: {bcolors.ENDC}")
    elif any(char in special_characters for char in test_letter):
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une lettre et non un caractère spécial{bcolors.ENDC}")
    else:
        print("Ok")

def cycle_letter(word, custom, string):
    test_letter = update_interface(word, custom, string)
    is_only_letter(test_letter, word)

def word_check(word):
    if len(word) < 1:
        clear_all()
        print(f"{bcolors.FAIL}Merci d'indiquer un mot{bcolors.ENDC}")
        ask_word()
    elif has_numbers(word):
        clear_all()
        print(f"{bcolors.FAIL}Merci de ne pas mettre de nombre dans le mot{bcolors.ENDC}")
        ask_word()
    else:
        if len(word.split()) > 1:
            clear_all()
            print(f"{bcolors.FAIL}Merci de mettre seulement un mot{bcolors.ENDC}")
            ask_word()
        elif any(char in special_characters for char in word):
            clear_all()
            print(f"{bcolors.FAIL}Merci de ne pas mettre de caractères spéciaux dans le mot{bcolors.ENDC}")
            ask_word()
        else:
            clear_all()
            word = word.upper()
            cycle_letter(word, False, None)
            

def ask_word():
    word = input(">> Quelle mot voulez vous faire deviner: ")
    word_check(word)

clear_all()
ask_word()