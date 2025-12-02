# 15. Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.

cadena = input("Escribe una cadena con vocales: ")
cadenaAsteriscos = ""
vocales = "aeiouAEIOU"
j = -1

for i in (cadena):
    j += 1
    if i in vocales:
        cadenaAsteriscos += "*"
    else:
        cadenaAsteriscos += cadena[j]
print(cadenaAsteriscos)