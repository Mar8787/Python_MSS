precioFinal = int(input("Introduce el precio final: "))
precioReal = int(input("Introduce el precio real: "))

porcentajeDescuento = ((precioReal - precioFinal) / precioReal) * 100

print("El porcentaje de descuento es:", round(porcentajeDescuento, 2), "%")