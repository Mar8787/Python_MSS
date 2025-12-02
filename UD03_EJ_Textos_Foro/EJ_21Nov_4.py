# 4. Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).

cadena = "Esta es una cadena larga"
cadenaNueva = ""

for i in range(len(cadena)):
    cadenaNueva = cadenaNueva + cadena[-i -1]
print(cadenaNueva)
