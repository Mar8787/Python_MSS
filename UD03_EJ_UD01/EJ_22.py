#* Crea un programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos son positivos y cuantos negativos.

pos = 0
neg = 0
contador = 0
while contador < 5:
    num = int(input("Introduce un número no nulo: "))
    if num == 0:
        print("El cero no es un número válido.")
    elif num > 0:
        contador += 1
        pos += 1
    else:
        contador += 1
        neg += 1
print(f"Números positivos: {pos}")
print(f"Números negativos: {neg}")