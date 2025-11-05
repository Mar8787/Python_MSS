#* Crea un programa que lea un valor correspondiente a una distancia en millas marinas y escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros.

millas = int(input("Introduce una distancia en millas: "))
metros = millas * 1.852
print(millas, "millas son", round(metros, 2), "kilómetros")