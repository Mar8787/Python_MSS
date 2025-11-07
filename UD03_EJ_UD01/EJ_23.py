#* Crea un programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.

pos = 0
neg = 0
num = float(input("Introduce un número no nulo o 0 para terminar: "))
while num != 0:
    if num > 0:
        pos += 1
    else:
        neg += 1
    num = float(input("Introduce un número no nulo o 0 para terminar: "))
if neg > 0:
    print("Se ha leído al menos un número negativo.")
    print(f"Números negativos: {neg}")
else:
    print("No se ha leído ningún número negativo.")
print(f"Números positivos: {pos}")