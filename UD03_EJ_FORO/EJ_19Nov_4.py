#Ejercicio 4: Cuadrado con diagonales y borde relleno.
#Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.

altura = 7

for i in range(altura):
    for j in range(altura):
        if (i == altura // 2 - 1 and j == altura - 2) or (i == altura // 2 + 1 and j == altura - 2):
            print(" ", end="")
        elif i == 0 or j == 0 or i == altura - 1 or j == altura - 1 or i + j == altura or i - j == -1:
            print("*", end="")
        else:
            print(" ", end="")
    print()