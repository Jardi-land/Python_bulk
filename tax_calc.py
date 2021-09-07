nombre = input("Entrer le montant:")
nombre = float(nombre)
nombre_4 = nombre - nombre/100*4
nombre_2 = nombre_4 - nombre_4/100*2
print("Montant restant:" + str(nombre_2))