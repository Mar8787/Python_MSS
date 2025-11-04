#* Ejercicio 21: Dibuja un programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído número negativo o no

neg = 0
for i in range(1, 5): #* Hacerlo con un while
    num = int(input("Introduce un número no nulo: "))
    if num == 0:
        print("El 0 no es un número válido. inténtelo de nuevo")
        i -= 1
    elif num > 0:
        continue
    else:
        neg += 1
if neg > 0:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")