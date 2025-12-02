# 55. Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de "Salir"

while (True):
    opcion = input("Menú. Pulsa el número indicado para cada ación: \n \
    1. Imprimir tu nombre en mayúsculas.\n \
    2. Ver el número secreo.\n \
    3. Salir.\n")
    match opcion:
        case "1":
            nombre = input("Escribe tu nombre: ")
            print(nombre.upper())
        case "2":
            print("1234")
        case "3":
            break
        case _:
            print("Pulsaste la tecla equivocada, inténtalo de nuevo.")