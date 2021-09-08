nombre = input(f"Entrer le montant: ")
if not nombre.isdigit():
#if type(nombre) != int or float:
    print("Merci d'entrer un nombre")
else:
    nombre = float(nombre)
    nombre_4 = nombre - nombre/100*4
    nombre_2 = nombre_4 - nombre_4/100*2
    print(f"Montant restant après les taxes: {str(nombre_2)}d")