from colors import bcolors
from pendu_var import special_characters, letter_devi, letter_good
from fc_interface import clear_all, letter_devi_fc, update_interface, game_over, win

HANGPHASE = 0

def has_numbers(string): return any(char.isdigit() for char in string)

def cycle_letter(word, custom, string, no_letter, hang_phase):
    test_letter = update_interface(word, custom, string, no_letter, hang_phase)
    is_only_letter(test_letter, word, no_letter, hang_phase)

def is_only_letter(test_letter, word, no_letter, hang_phase):
    clear_all()
    if len(test_letter) < 1: cycle_letter(word, True, f">> {bcolors.FAIL}Merci d'indiquer une lettre: {bcolors.ENDC}", no_letter, hang_phase)
    elif has_numbers(test_letter):
        cycle_letter(word, True,f">> {bcolors.FAIL}Merci de mettre une lettre et non un nombre: {bcolors.ENDC}", no_letter, hang_phase)
    elif len(test_letter) > 1: cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une seule lettre: {bcolors.ENDC}", no_letter, hang_phase)
    elif any(char in special_characters for char in test_letter):
        cycle_letter(word, True, f">> {bcolors.FAIL}Merci de mettre une lettre et non un caractère spécial: {bcolors.ENDC}", no_letter, hang_phase)
    elif letter_devi.count(test_letter.upper()) == 1:
        cycle_letter(word, True,f">> {bcolors.FAIL}Vous avez déjà essayé cette lettre: {bcolors.ENDC}", no_letter, hang_phase)
    elif letter_good.count(test_letter.upper()) == 1: cycle_letter(word, True, f">> {bcolors.FAIL}Vous avez déjà essayé cette lettre: {bcolors.ENDC}", no_letter, hang_phase)
    else:
        is_in_list = letter_devi_fc(test_letter.upper(), word)
        if is_in_list:
            for i in range(word.count(test_letter.upper())):
                if i > 0: insert_pos = word.index(test_letter.upper(), last_pos)
                else: insert_pos = word.index(test_letter.upper())
                no_letter.pop(insert_pos)
                no_letter.insert(insert_pos, test_letter.upper())
                last_pos = insert_pos + 1
            letter_good.append(test_letter.upper())
            if word == no_letter:
                want_replay = win(word, hang_phase, no_letter)
                if want_replay:
                    clear_all()
                    letter_devi.clear()
                    letter_good.clear()
                    ask_word()
                else: clear_all()
            else: cycle_letter(word, False, None, no_letter, hang_phase)
        else:
            hang_phase = hang_phase + 1
            if hang_phase == 8:
                want_replay = game_over(word, hang_phase, no_letter)
                if want_replay:
                    clear_all()
                    letter_devi.clear()
                    letter_good.clear()
                    ask_word()
                else:
                    clear_all()
            else:
                letter_devi.append(test_letter.upper())
                cycle_letter(word, False, None, no_letter, hang_phase)

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
            word = list(word.upper())
            for i in word:
                no_letter.append("_")
            for i in range(len(word)):
                letter_good.insert(i, "_")
            hang_phase = HANGPHASE
            cycle_letter(word, False, None, no_letter, hang_phase)

def ask_word():
    word = input(">> Quelle mot voulez vous faire deviner: ")
    word_check(word)

clear_all()
ask_word()
