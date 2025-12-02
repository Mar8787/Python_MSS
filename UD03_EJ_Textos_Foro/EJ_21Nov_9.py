# 9. Leer una cadena y contar cuántas vocales contiene.

cadena = input("Introduce una palabra o una frase para contar sus vocales: ")
vocales = "aeiouAEIOU"
contador = 0

for i in cadena:
    if i in vocales:
        contador += 1
print(f"En tu cadena hay {contador} vocales.")