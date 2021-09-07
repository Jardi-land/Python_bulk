nombre = input("Entrer le montant: \033[94m")
nombre = float(nombre)
nombre_4 = nombre - nombre/100*4
nombre_2 = nombre_4 - nombre_4/100*2
print("\033[0mMontant restant après les taxes: \033[94m" + str(nombre_2) + "\033[0m")