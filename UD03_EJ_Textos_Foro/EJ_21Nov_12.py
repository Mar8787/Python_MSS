# 12. Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.

cadena = input("Introduce una cadena de texto: ")
cadenaInversa = ""

print("\n====Forma 1====")
for i in range(len(cadena)):
    cadenaInversa += cadena[-i -1]
print(cadenaInversa)

print("\n====Forma 2====")
cadenaInversa = (cadena[::-1])
print(cadenaInversa)

