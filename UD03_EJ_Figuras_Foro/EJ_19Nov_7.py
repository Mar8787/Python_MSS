#Ejercicio 7: Letra B.
#Imprime un triángulo invertido de altura n con asteriscos en el borde, y líneas internas de relleno alternadas entre espacios y asteriscos.
altura = 6
#altura = int(input("Imprime una altura para la figura: "))

print("*" * altura)
for i in range(altura):
    for j in range(altura):
        if i == altura - 1 :
            print("*", end="")
        if i % 2 == 0:
            print("*", end=" ")
    print()