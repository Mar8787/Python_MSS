altura = int(input("Introduce la altura del triángulo: "))
for i in range(1, altura + 1):
    for j in range(0-1, i-1):
        print(" ", end="")
    for k in range(0, (2 * altura + 1) - (i * 2)):
        print("*", end="")
    print("")