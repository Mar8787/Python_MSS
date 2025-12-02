# 5. Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.

cadena = "El jefe pedro Pechaca"
caracter = input("Escribe un caracter para buscar: ")
bandera = False

for i in cadena:
    if i == caracter:
        bandera = True

if bandera:
    print(f"El caracter '{caracter}' se encuentra en la cadena.")
else:
    print(f"El caracter '{caracter}' no se encuentra en la cadena.")