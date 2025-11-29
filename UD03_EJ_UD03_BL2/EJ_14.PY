# 14. Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura de la pirámide por teclado.


altura = int(input("Introduce la altura del triángulo: "))
print("\n############### Versión 1 ###############\n")
for i in range(1, altura + 1):
    # Se construyen los espacios
    for j in range(i, altura):
        print(" ", end="")
    # Se construyen los *
    for k in range(1, (2 * i)):
        print("*", end="")
    print("")

print("\n############### Versión 2 ###############")
