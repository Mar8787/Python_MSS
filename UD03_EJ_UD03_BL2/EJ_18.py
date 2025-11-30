# 18. Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia (^), siendo A y B valores introducidos por teclado,
# y luego muestre el resultado por pantalla.

a = int(input("Introduce un número entero: "))
b = int(input("Introduce su potencia: "))

resultado = 1

for i in range(b):
    resultado = resultado * a
print(resultado)