# 17. Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.

cadena = input("Introduzca una cadena: ")
cadenaRepe = ""

for i in cadena:
     if cadena.count(i) > 1:
         cadenaRepe += i
print(cadenaRepe)