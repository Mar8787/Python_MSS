# 22. Escriba un programa que recibe como datos de entrada una hora expresada en horas, minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán, transcurrido un segundo

horaCompleta = input("Introduce la hora en formato HH:MM:SS -> ")

horaPartes = horaCompleta.split(":")

h = int(horaPartes[0])
m = int(horaPartes[1])
s = int(horaPartes[2])

if s == 59 and m == 59 and h == 24:
    s = 00
    m = 00
    print(f"1:{m}:{s} h")

elif s == 59 and m == 59:
    s = 00
    m = 00
    h = h + 1
    print(f"{h}:{m}:{s} h")
elif s == 59:
    s = 00
    m = m + 1
    print(f"{h}:{m}:{s} h")
else:
    s = s + 1
    print(f"{h}:{m}:{s} h")









#Se puede usar map, darle una vuelta