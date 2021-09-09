from colors import bcolors
from pendu_var import *
from fc_interface import *

hangphase = 0

def has_numbers(string):
    return any(char.isdigit() for char in string)

def cycle_letter(word, custom, string, no_letter, hangphase):
    test_letter = update_interface(word, custom, string, no_letter, hangphase)
    is_only_letter(test_letter, word, no_letter, hangphase)

def is_only_letter(test_letter, word, no_letter, hangphase):
    clear_all()
    if len(test_letter) < 1:
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci d'indiquer une lettre: {bcolors.ENDC}", no_letter, hangphase)
    elif has_numbers(test_letter):
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une lettre et non un nombre: {bcolors.ENDC}", no_letter, hangphase)
    elif len(test_letter) > 1:
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une seule lettre: {bcolors.ENDC}", no_letter, hangphase)
    elif any(char in special_characters for char in test_letter):
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une lettre et non un caractère spécial: {bcolors.ENDC}", no_letter, hangphase)
    elif letter_devi.count(test_letter.upper()) == 1:
        cycle_letter(word, True, f">> {bcolors.FAIL}Vous avez déjà essayé cette lettre: {bcolors.ENDC}", no_letter, hangphase)
    elif letter_good.count(test_letter.upper()) == 1:
        cycle_letter(word, True, f">> {bcolors.FAIL}Vous avez déjà essayé cette lettre: {bcolors.ENDC}", no_letter, hangphase)
    else:
        is_in_list = letter_devi_fc(test_letter.upper(), word)
        if is_in_list:
            for i in range(word.count(test_letter.upper())):
                if i > 0:
                    insert_pos = word.index(test_letter.upper(), last_pos)
                else:
                    insert_pos = word.index(test_letter.upper())
                no_letter.pop(insert_pos)
                no_letter.insert(insert_pos, test_letter.upper())
                last_pos = insert_pos + 1
            letter_good.append(test_letter.upper())
            if word == no_letter:
                want_replay = win(word, hangphase, no_letter)
                if want_replay:
                    clear_all()
                    letter_devi.clear()
                    letter_good.clear()
                    ask_word()
                else:
                    clear_all()
            else:
                cycle_letter(word, False, None, no_letter, hangphase)
        else:
            hangphase = hangphase + 1
            if hangphase == 8:
                want_replay = game_over(word, hangphase, no_letter)
                if want_replay:
                    clear_all()
                    letter_devi.clear()
                    letter_good.clear()
                    ask_word()
                else:
                    clear_all()
            else:
                letter_devi.append(test_letter.upper())
                cycle_letter(word, False, None, no_letter, hangphase)

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
            no_letter = []
            word = [char for char in word.upper()]
            for i in word:
                no_letter.append("_")
            for i in range(len(word)):
                letter_good.insert(i, "_")
            cycle_letter(word, False, None, no_letter, hangphase)

def ask_word():
    word = input(">> Quelle mot voulez vous faire deviner: ")
    word_check(word)

clear_all()
ask_word()