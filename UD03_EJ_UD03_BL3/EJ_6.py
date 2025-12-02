# 6. Calcular la media de tres números pedidos por teclado.

num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce otro número: "))
num3 = float(input("Introduce el último número: "))
media = 0.00

media = (num1 + num2 + num3) / 3

print(f"La media de {num1}, {num2} y {num3} es: {media:.2f}")
