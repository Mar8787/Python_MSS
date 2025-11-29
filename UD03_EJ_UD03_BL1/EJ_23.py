# 23. Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente:
# Si el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta” se incrementa un recargo del 3% al valor de compra.
# Calcular y visualizar el descuento o recargo según sea el caso y el total a pagar de la compra.

print("Programa para ingtresar el valor de compra.")
importe = float(input("Introduzca el importe: "))
modoPago = input(" -Si el modo de pago es en efectivo pulse 1. \n -Si es en tarjeta, pulse 2: ")

match modoPago:
    case "1":
        precioFinal = importe * 0.95
    case "2":
        precioFinal = importe * 1.03
print(f"El precio final de la compra es de: {precioFinal}€")