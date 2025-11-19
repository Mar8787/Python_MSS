altura = int(input("Introduce la altura de la figura: "))

#Cabecera de la figura
print((altura+1)*(" ") + "*")

#Esto nos da la altura
for i in range(1, altura + 1):

    #construimos los espacios delanteros
    for j in range(i, altura):
        print(" ", end="")

    #construimos el * los espacios de en mendio y el * final
    print("*", end="")
    for k in range(1, i + 1):
        print(" ", end="")
    print("*", end="")
    print("")

#Segunda parte de la figura
for i in range(1, altura):
    for j in range(0 - 1, i - 1):
        print(" ", end="")
    print("*", end="")
    for k in range(0, (altura + 1) - (i + 1)):
        print(" ", end="")
    print("*", end="")
    print("")
print((altura + 1) * (" ") + "*")