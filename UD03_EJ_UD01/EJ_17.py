#* Ejerccicio 17: Dibuja un programa que lea dos números y lo visualiza en orden ascendente

a = int(input("Intoduce un número entero: "))
b = int(input("Introduce un número entero distinto: "))
if a == b:
    print("Los números son iguales.")
elif a > b:
    print(f"El número {a} es mayor que {b}.")
else:
    print(f"El número {b} es mayor que {a}.")