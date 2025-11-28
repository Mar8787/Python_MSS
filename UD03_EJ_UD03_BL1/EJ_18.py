# 18. Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10

num = int(input("Introduce un numero entero para saber si es múltiplo de 10: "))
if num % 10 == 0:
    print(f"{num} es múltiplo de 10.")
else:
    print(f"{num} no es múltiplo de 10.")