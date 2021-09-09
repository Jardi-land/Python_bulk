from colors import bcolors
from pendu_var import *
from fc_interface import *

def has_numbers(string):
    return any(char.isdigit() for char in string)

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
            update_interface()


def ask_word():
    word = input(">> Quelle mot voulez vous faire deviner: ")
    word_check(word)

clear_all()
ask_word()