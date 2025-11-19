altura = int(input("Introduce la altura de la figura: "))
#Cabecera de la figura
print(altura*(" ") + "*")

for i in range(1, altura + 1):
    #construimos los primeros espacios
    for j in range(i, altura):
        print(" ", end="")
    #construimos el *
    for k in range(1, i +2):
        print("*", end="")
    print("")
    
