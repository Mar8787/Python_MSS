# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

import math

catetoA = float(input("Introduce el valor del cateto a: "))
catetoB = float(input("Introduce el valor del cateto b: "))
hipotenusa = 0.00

hipotenusa = math.sqrt(catetoA**2 + catetoB**2)

print(f"La hipotenusa es: {hipotenusa: .2f}")
