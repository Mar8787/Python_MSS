# Ejercicio 3: Bloques de 3x3.

altura = int(input("Introduce una altura: "))

for i in range(altura * 3):
    for j in range(altura * 3):

        # Bloque gordo 3x3
        bloqueFila = i // 3
        bloqueColumna = j // 3

        # Pintamos los bloques gordos impares
        if (bloqueFila + bloqueColumna) % 2 == 1:
            print("*", end=" ")
        # Dejamos los bloques  gordos pares vacíos
        else:
            print(" ", end=" ")
    print()
