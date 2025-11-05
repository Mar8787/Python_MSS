#* Crea un programa que dado el precio de un artículo y el precio de venta real nos muestre el porcentaje de descuento realizado.

precioFinal = int(input("Introduce el precio final: "))
precioReal = int(input("Introduce el precio real: "))

porcentajeDescuento = ((precioReal - precioFinal) / precioReal) * 100

print("El porcentaje de descuento es:", round(porcentajeDescuento, 2), "%")