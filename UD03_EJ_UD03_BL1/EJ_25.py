# 25. La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el postulante.
# Ingrese por teclado el nombre del postulante y la facultad que va a estudiar,
# muestre el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el control switch).

print("Bienvenido a la Universidad Privada de Cádiz")
nombre = input("Ingrese su nombre: ")
print("\nEsta es la lista de códigos para facultades: \n-Facultad de Ciencias de la Salud: ccss \n-Facultad de Ingeniería: ingenieria \
    \n-Facultad de Humanidades: humanidades \n-Facultad de Ciencias Ambientales: ccaa")

facultad = input("\nIngrese el código de su facultad: ")
codigo = facultad.lower()

match codigo:
    case "ccss":
        matricula = 800.0
        mensualidad = 550.0
        iva = matricula * 0.18 + mensualidad * 0.18
        montoFinal = matricula + mensualidad + iva
        nombreFacultad = "Facultad: Facultad de Ciencias de la Salud"
    case "ingenieria":
        matricula = 890.0
        mensualidad = 600.0
        iva = matricula * 0.18 + mensualidad * 0.18
        montoFinal = matricula + mensualidad + iva
        nombreFacultad = "Facultad de Ingeniería"
    case "humanidades":
        matricula = 750.0
        mensualidad = 520.0
        iva = matricula * 0.18 + mensualidad * 0.18
        montoFinal = matricula + mensualidad + iva
        nombreFacultad = "Facultad: Facultad de Humanidades"
    case "ccaa":
        matricula = 800.0
        mensualidad = 550.0
        iva = matricula * 0.18 + mensualidad * 0.18
        montoFinal = matricula + mensualidad + iva
        nombreFacultad = "Facultad de Ciencias Ambientales"
    case _:
        print("Facultad no encontrada. Comience de nuevo.")
if codigo != "ccss" or "ingenieria" or "humanidades" or "ccaa":
    print("")
else:
    print(f"\nNombre postulante: {nombre}")
    print(f"Facultad: {nombreFacultad}")
    print(f"Matrícula: {matricula}€ \nMensualidad: {mensualidad}€ \nIVA: {iva}€ \nMonto final: {montoFinal}€")