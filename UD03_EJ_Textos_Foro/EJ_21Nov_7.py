# Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.

cadenaVieja = "camaleon"
cadenaNueva = ""
caracterNuevo = input("Introduce un caracter nuevo: ")
posicion = int(input("Di la posición donde quieres introducir el caracter nuevo: "))

for i in range(len(cadenaVieja)):
    if i == posicion:
        cadenaNueva = cadenaNueva + cadenaVieja[:i] + caracterNuevo + cadenaVieja[i+1:]
print(cadenaNueva)