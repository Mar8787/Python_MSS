# 11. Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

cadenaOriginal = input("Introduce una cadena: ")
cadenaNueva = ""
vocales = "aeiouAEIOU"
j = -1

for i in cadenaOriginal:
    j += 1
    if i in vocales:
        cadenaNueva += cadenaOriginal[j] * 2
    else:
        cadenaNueva += cadenaOriginal[j]
print(cadenaNueva)