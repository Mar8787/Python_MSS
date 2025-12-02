# 18.  Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).

cadena = input("Escribe una cadena: ")
cadenaNueva = ""
vocales = "aeiouAEIOU"

for i in cadena:
    if i in vocales:
        cadenaNueva = cadenaNueva
    else:
        cadenaNueva += i
print(cadenaNueva)