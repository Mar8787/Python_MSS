#* Ejercicio 20: Dibuja un programa que lea un número positivo N y calcule y visualice su factorial N!

num = int(input("Introduce un número positivo: "))
if num >= 0:
    if 0 <= num <= 1:
        print(f"{num}!=1")
    else:
        facto = 1
        for i  in range(1, num + 1):
            facto *= i
        print(f"{num}!={facto}")
else:
    print("El número introducido no es positivo.")