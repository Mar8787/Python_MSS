#* Ejercicio 15: Dibuja un programa que lee dos números y muestra el mayor.

a = int(input("Introduzce un número entero: "))
b = int(input("Introduzce otro número entero: "))
if a > b:
    print(f"El número {a} es mayor que {b}.")
else:
    print(f"El número {b} es mayor que {a}.")