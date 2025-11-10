# Crea un programa que lea una secuencia de notas (con valores que van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.

nota = 0
contador = 0
while nota != -1:
    nota = float(input("Introduce una nota (o -1 para terminar): "))