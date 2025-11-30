#Ejercicio 2: Estrella de ocho puntas.
# Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).

altura = 9

for i in range(altura):
    for j in range(altura):
        if i == altura // 2 or j == altura // 2 or i == j or i + j == altura - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()