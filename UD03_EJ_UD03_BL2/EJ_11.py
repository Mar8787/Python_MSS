# 11. Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de la escalera por teclado.

altura = int(input("Introduce la altura de la escalera: "))

# Uso i y j para llenar los huecos de la matriz que quiera. i Filas, j columnas, diagonal, cuando i = j, se rellena de la diagonal hacia abajo.
for i in range(altura):
    for j in range(altura):
        if j <= i:
            print("*", end=" ")
    print()