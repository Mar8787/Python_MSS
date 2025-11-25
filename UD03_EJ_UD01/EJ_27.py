# 27 Crea un programa que lea una secuencia de notas (con valores que van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.

nota = 0
contador = 0
while nota != -1:
    nota = float(input("Introduce una nota (o -1 para terminar): "))
    if 0 <= nota <= 10:
        if nota == 10:
            contador += 1
    else:
        print(f"Introduce una nota válida")
if contador > 0:
    print("Detectada al menos una nota con valor 10.")
else:
    print("No se ha detectado ninguna nota con valor 10.")