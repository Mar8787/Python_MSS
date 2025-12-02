# 56. Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad de números primos que queremos mostrar.

cantidadPrimos = int(input("Introduce los números primos que quieres ver: "))
contador = 0
numero = 2

while contador < cantidadPrimos:
    esPrimo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            esPrimo = False
    if esPrimo:
        print(numero)
        contador += 1
    numero += 1