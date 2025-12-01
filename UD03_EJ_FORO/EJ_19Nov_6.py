#Ejercicio 6: Letra M mayúscula con asteriscos
#Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.
altura = 7

for i in range(altura):
    for j in range(altura):
        if (j == 1 and i == altura - 2) or (j == 2 and i == altura // 2 + 1) or (j == altura - 2 and i == altura - 2) or j == altura // 2 + 1 and i == altura // 2 + 1:
            print(" ", end="")
        elif j == 0 or j == altura - 1 or j == i or i + j == altura -1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

