# 8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y
# el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

venta1 = float(input("Introduce el importe de la venta 1: "))
venta2 = float(input("Introduce el importe de la venta 2: "))
venta3 = float(input("Introduce el importe de la venta 3: "))
sueldoBase = float(input("Introduce el importe del sueldo base: "))
sueldoTotal = 0.00

comision = venta1 * 0.10 + venta2 * 0.10 + venta3 * 0.10
sueldoTotal = sueldoBase + comision

print(f"Comisiones: {comision: .2f}, sueldo final: {sueldoTotal:.2f}")

