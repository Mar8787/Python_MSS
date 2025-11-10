#* Programa que calcula el salario neto semanal de un trabajador en función del número de horas trabajadas y la tasa de impuestos

nombre = input("Introduce el nombre del trabajador: ")
precio_hora = float(input("Introduce el precio por hora trabajada: "))
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * precio_hora
else:
    hora_doble = horas_trabajadas - 35
    salario_bruto = (35 * precio_hora) + (hora_doble * precio_hora * 2)
if salario_bruto <= 500:
    print(f"Salario de {nombre}: {salario_bruto}")
else:
    bruto_25 = salario_bruto - 500
    if bruto_25 <= 400:
        tasas = bruto_25 * 0.25
        neto = 500 - tasas
    else:
        tasas = bruto_25
        bruto_45 = bruto_25 - 400
        tasas += bruto_45 * 0.45
        neto = salario_bruto - tasas
    print(f"{nombre}, salario bruto: {salario_bruto}, tasas: {tasas}, salario neto: {neto}")