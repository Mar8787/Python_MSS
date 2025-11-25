# 29 Crea un programa donde el usuario “piensa” un número del 1 al 100 y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al número pensado).

min = 1
max = 100
respuesta = 0
bandera = True

while bandera:
    propuesta = (min + max) // 2
    respuesta = int(input(f"Si tu número es {propuesta}, pulsa 1. Si no lo es, pulsa 0 :"))

    if respuesta != 1:
        respuesta = int(input(f"¿Tu número es mayor que {propuesta}? Pulsa 1 si es verdad, 0 si no lo es: "))
        if respuesta == 1:
            min = propuesta + 1
        else:
            max = propuesta - 1
    else:
        print(f"Tu número es {propuesta}.")
        bandera = False