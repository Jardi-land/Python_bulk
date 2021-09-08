nombre_1 = input("Votre premier nombre: ")
if not nombre_1.isdigit():
    print("Merci de rentrer un nombre")
else:
    nombre_2 = input("Votre deuxieme nombre: ")
    if not nombre_2.isdigit():
        print("Merci de rentrer un nombre")
    else:
        nombre_1 = float(nombre_1)
        nombre_2 = float(nombre_2)
        print(f"le résultat est: {nombre_1 + nombre_2}")