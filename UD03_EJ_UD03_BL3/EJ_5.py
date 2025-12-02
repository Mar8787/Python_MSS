# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

gradosF = float(input("Introduce grados Fahrenheit: "))
gradosC = 0.00

gradosC = (gradosF - 32) * 5 / 9

print(f"{gradosF} Fº = {gradosC: .2f} Cº")