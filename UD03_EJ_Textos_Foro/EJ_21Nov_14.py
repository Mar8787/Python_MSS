# 14. Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.

cadena = input("Introduce una cadena con números y letras: ")
contador = 0

for i in cadena:
    if i.isdigit():
        contador += 1
print(f"Hay {contador} núeros en tu cadena.")