# 15. Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos la altura de la pirámide por teclado.

altura = int(input("Introduce la altura del triángulo: "))

print("\n############### Versión 1 ###############\n")

for i in range(1, altura + 1):
    for j in range(0-1, i-1):
        print(" ", end="")
    for k in range(0, (2 * altura + 1) - (i * 2)):
        print("*", end="")
    print("")

print("\n############### Versión 2 ###############")

for i in range(altura):
    for j in range((altura * 2) - 1):
        if (j - i) >= 0 and (i + j) <= (altura * 2) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()