#Ejercicio 1: Diamante hueco. Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.

altura = int(input("Introduce el valor de la altura de la figura: "))

for i in range(0, (altura * 2) - 1):
    for j in range(0, (altura * 2) - 1):
        if i + j == altura - 1 or j - i == altura - 1 or i - j == altura -1 or i + j == altura * 2 + 2:
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print("")