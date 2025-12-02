# Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).

cadenaMinus = "hola"
cadenaMayus = ""

for i in range(len(cadenaMinus)):
    cadenaMayus += chr(ord(cadenaMinus[i]) - 32)
print(cadenaMayus)