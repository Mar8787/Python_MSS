#* Crea un programa que lea tres números y nos diga cual es mayor, cual menor y cuales son iguales.

a = int(input("Introduce un número entero: "))
b = int(input("Introduce otro número entero: "))
c = int(input("Introduce un número entero más: "))
if a > b:
    if a == c:
        print(f"{a} > {b} = {c}")
    elif a > c:
        if b > c:
            print(f"{a} > {b} > {c}")
        elif b == c:
            print(f"{a} > {b} = {c}")
        else:
            print(f"{a} > {c} > {b}")
    else:
        print(f"{c} > {a} > {b}")
elif a == b:
    if b > c:
        print(f"{a} = {b} > {c}")
    elif b == c:
        print(f"{a} = {b} = {c}")
    else:
        print(f"{c} > {a} = {b}")
elif b > c:
    if a > c:
        print(f"{b} > {a} > {c}")
    elif a == c:
        print(f"{b} > {a} = {c}")
    else:
        print(f"{b} > {c} > {a}")
elif b == c:
    print(f"{b} = {c} > {a}")
else:
    print(f"{c} > {b} > {a}")