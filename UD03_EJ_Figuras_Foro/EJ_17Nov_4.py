#Ejercicio 4: Rejilla de un espacio.

altura = int(input("Introduce la altura de la figura: "))

#Cabecera de la figura
print(((altura * 2) + 1) * ("* "))

#Altura de la figura
for i in range(1, altura + 1):
    print("*   " * (altura + 1))
    print("* " * (((altura + 1 ) * 2) - 1))