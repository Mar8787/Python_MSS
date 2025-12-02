# Ejercicio 8: Rombo sólido.
# Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.
altura = 4
# n = int(input("Introduce el valor de la variable n para dubujar un rombo: "))

for i in range(altura):
    for j in range(altura - i - 1):
        print(" ", end="")

    for k in  range(2 * i + 1):
        print("*", end="")
    print()

for i in range(altura - 2, -1, -1):
    for j in range(altura - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end="")
    print()