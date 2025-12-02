# 16. Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).

cadena1 = "Hola"
cadena2 = "amiga"
concat = ""

for i in cadena1, " ", cadena2:
    concat += i
print(concat)