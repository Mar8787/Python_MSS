#* Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual menor y cuales son iguales.

a = int(input("Introduce un número entero: "))
b = int(input("Introduce otro número entero: "))
c = int(input("Introduce un número entero más: "))
if a == b and b==c:
    print(f"{a}, {b} y {c} son iguales.")
elif a > b and a > c:
        if b > c:
            print(f"Mayor: {a}. Menor: {c}. Intermedio: {b}.")
        elif b == c:
            print(f"Mayor: {a}. Menores e iguales: {b} y {c}.")
        else:
            print(f"Mayor: {a}. Menor: {b}. Intermedio: {c}.")
if a == c:
    print(f"Mayor: {b}. Menores e iguales: {a} y {c}.")
elif b == c:
    print(f"Menor: {a}. Mayores e iguales: {b} y {c}.")
elif b > c:
    print(f"Mayor: {b}. Menor: {a}. Intermedio: {c}.")    
else:
    print(f"Mayor: {c}. Menor: {a}. Intermedio: {b}.")