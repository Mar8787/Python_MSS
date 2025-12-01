#Ejercicio 6: Letra M mayúscula con asteriscos
#Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.
altura = int(input("Introduce la altura de la M: "))

altura1cuarto = altura // 2 + 1

for i in range(altura1cuarto):
    for j in range(altura1cuarto * 2):
        if j == 0 or i == j or j + i == altura1cuarto * 2 - 2 or j == altura1cuarto * 2 - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(altura1cuarto - 1):
    for j in range(altura1cuarto * 2):
        if j == 0 or j == altura1cuarto * 2 - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()