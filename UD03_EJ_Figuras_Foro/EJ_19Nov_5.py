#Ejercicio 5: Cruz con borde punteado.
#Imprime una cruz en una matriz de tamaño n x n con puntos en el borde, asteriscos en las líneas vertical y horizontal centrales, y espacios en el resto.

altura = int(input("Introduce una altura para "))

for i in range(altura):
    for j in range(altura):
        if j == 0 and i == altura // 2 or j == altura - 1 and i == altura // 2:
            print("*", end=" ")
        elif i == 0 or i == altura - 1 or j == 0 or j == altura - 1 or (j == altura // 2 and i == altura // 2 - 1) or (j == altura // 2 and i == altura // 2 + 1):
            print(".", end=" ")
        elif i == j or i + j == altura - 1 or i == altura // 2 or j == altura // 2:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()