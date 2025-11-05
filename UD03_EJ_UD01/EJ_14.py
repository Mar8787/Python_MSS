#* Ejercicio 14: Crea un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división (Ten en cuenta la división por cero).

a = int(input("Introduce un número entero: "))
b = int(input("Introduce otro número entero: "))
suma = a + b
resta = a - b
producto = a * b
division = a / b
if b == 0:
    print("Suma:", a, "+", b, "=", suma)
    print("Resta:", a, "-", b, "=", resta)
    print("Producto:", a, "*", b, "=", producto)
    print("No se puede dividir entre cero.")
else:
    print("Suma:", a, "+", b, "=", suma)
    print("Resta:", a, "-", b, "=", resta)
    print("Producto:", a, "*", b, "=", producto)
    print("División:", a, "/", b, "=", round(division, 2))