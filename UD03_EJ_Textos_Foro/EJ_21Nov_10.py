# Leer una cadena y contar cuántos caracteres son letras mayúsculas.

cadena = input("Introduce una cadena para contar sus mayúsulas: ")
contador = 0

for i in cadena:
    if i.isupper():
        contador += 1
print(contador)