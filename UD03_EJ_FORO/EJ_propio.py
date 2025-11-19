altura = int(input("Introduce la altura de la figura: "))
#Cabecera de la figura
print(altura*(" ") + "*")

for i in range(1, altura + 1):
    #construimos los espacios
    for j in range(i, altura):
        print(" ", end="")
    #construimos el *
    for k in range(1, i + 2):
        print("*", end="")
    print("")

#Segunda parte de la figura
for i in range(1, altura + 1):
    for j in range(0 - 1, i - 1):
        print(" ", end="")
    for k in range(0, (altura + 2) - (i + 1)):
        print("*", end="")
    print("")