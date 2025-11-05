#* Ejercicio 18. Cera un programa que lea dos números y nos diga cual es mayor o si son iguales.

a = int(input("Introduce un número entero: "))
b = int(input("Introduce un número entero distinto: "))
if a >= b:
    if a == b:
        print(f"{a} es igual que {b}.")
    else:
        print(f"{a} es mayor que {b}.")
else:
    print(f"{b} es mayor que {a}.")
