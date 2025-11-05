#* Ejercicio 21: Crea un programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído número negativo o no

neg = 0
contador = 0
while contador < 100:
    num = int(input("Introduce un número no nulo: "))
    if num == 0:
        print("El cero no es un número válido.")
    elif num > 0:
        contador += 1
    else:
        contador += 1
        neg += 1
if neg > 0:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")