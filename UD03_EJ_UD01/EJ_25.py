#* Crea un programa que lea una calificación numérica entre 0 y 10 y la transforme en la calificación alfabética,

nota = float(input("Introduce tu nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
elif nota >= 3:
    print("Insuficiente")
else:
    print("Muy deficiente")
