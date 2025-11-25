# 28 Crea un programa que sume independientemente los pares y los impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas sumas.

pares = 0
impares = 0
for i in range(100, 201):
    if i%2 == 0:
        pares = pares + i
    else:
        impares = impares + i
print(f"La suma de los números pares es {pares} y la suma de los impares es {impares}")