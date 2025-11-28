# 19. Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, con el siguiente menú de opciones: 
# Bienvenido a su Cajero Virtual 
# 1. Ingresar dinero en cuenta 
# 2. Retirar dinero de la cuenta 
# 3. Salir

opcion = " "

while opcion != ("3"):
    print("Bienvenido a su Cajero Virtual.") 
    print("Pulse 1 para ingresar dinero en cuenta.")
    print("Pulse 2 para retirar dinero de la cuenta.")
    print("Pulse 3 para salir. ")
    opcion = input("")
    match opcion:
        case "1":
            print("Ha elegido ingresar")
        case "2":
            print("Ha elegido retirar")
        case "3":
            print("Gracias, buenas tardes.")
        case _:
            print("Opción incorrecta, comience de nuevo.")