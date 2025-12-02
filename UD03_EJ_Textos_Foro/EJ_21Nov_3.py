# 3. Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

cadena = input("Introduce un string: ")
cararter = input("Introduce un caracter para buscar: ")
contador = 0

for i in cadena:
    if i == cararter:
        contador+=1
print(f"Hay {contador} '{cararter}' en la cadena '{cadena}'")