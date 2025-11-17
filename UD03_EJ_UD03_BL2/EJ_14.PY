altura = int(input("Introduce la altura del triángulo: "))
for i in range(1, altura + 1):
    # Se construyen los espacios
    for j in range(i, altura):
        print(" ", end="")
    # Se construyen los *
    for k in range(1, (2 * i)):
        print("*", end="")
    print("")