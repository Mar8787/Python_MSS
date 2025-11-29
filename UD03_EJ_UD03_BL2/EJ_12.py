# 12. Crea una aplicación que dibuje una escalera de números, siendo cada línea un número. Nosotros le pasamos la altura por teclado.

altura = int(input("Introduce la altura de la escalera: "))

for i in range(altura):
    for j in range(altura):
        if j <= i:
            print(i+1, end=" ")
    print()