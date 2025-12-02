# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

minutos = int(input("Introduce una cantidad de minutos: "))
horas = 0
resto = 0

horas = minutos // 60
resto = minutos % 60

if resto != 0:
    minutos = resto
else:
    minutos = 0

print(f"Transformación horaria: {horas:02d}:{minutos:02d} h")