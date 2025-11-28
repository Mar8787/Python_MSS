# 16. Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene

num = int(input("Introduce un número entero entre 0 y 99999: "))
cifras = 0
if 0 <= num <= 99999:
    while num != 0:
        num = num // 10
        cifras = cifras + 1
print(f"El número {num} tiene {cifras} cifras")