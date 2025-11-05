#* Crea un programa que toma como dato de entrada un número que corresponde a la longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera que corresponde con dicho radio.

radio = int(input("Introduce un valor para radio: "))

longitud = 2 * 3.14 * radio
area = 3.14 * radio**2
volumen = (4/3) * 3.14 * radio**3

print("La longitud de la circunferencia es: ", round(longitud, 2))
print("El área del círculo es: ", round(area, 2))
print("El volumen de la esfera es: ", round(volumen, 2))
