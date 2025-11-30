#Ejercicio 3: Pirámide con huecos internos (estructura tipo "reja")
#Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.
altura = 6
# altura = int(input("Introduce una altura: "))

for i in range(altura):
    for j in range((altura * 2) - 1):
        if i + j == altura - 1 or j - i == altura -1 or i == altura - 1:
            print("*", end=" ")
        elif i == altura // 2 and i + j > altura - 1 and j - i < altura - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()