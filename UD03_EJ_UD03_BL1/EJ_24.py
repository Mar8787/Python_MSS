# 24. Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día de la semana;
# si el día es martes o jueves, se realizará un descuento del 15% por la compra. Visualizar el descuento y el total a pagar por la compra.

print("Programa para ingresar el valor de la compra.")
importe = float(input("Introduzca el importe de la compra: "))
diaSemana = input("Introduzca el día de la semana: ")
diaSemanaMinus = diaSemana.lower()

match diaSemanaMinus:
    case "martes" | "jueves":
        precioFinal = importe * 0.85
        print(f"Importe final con descuento del 15% aplicado: {precioFinal}")
    case "lunes" | "miercoles" | "viernes":
        print(f"Importe final sin descuento aplicado: {importe}")
    case _:
        print("Día de la semana no válido. Empiece de nuevo.")