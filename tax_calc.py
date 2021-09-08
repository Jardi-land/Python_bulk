from colors import bcolors

nombre = input(f"Entrer le montant: {bcolors.OKBLUE}")
if not nombre.isdigit():
#if type(nombre) != int or float:
    print(f"{bcolors.ENDC}Merci d'entrer un nombre")
else:
    nombre = float(nombre)
    nombre_4 = nombre - nombre/100*4
    nombre_2 = nombre_4 - nombre_4/100*2
    print(f"{bcolors.ENDC}Montant restant après les taxes: {bcolors.OKBLUE + str(nombre_2) + bcolors.ENDC}")