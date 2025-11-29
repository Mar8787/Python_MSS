# 13. Crea una aplicación que dibuje una escalera de números, siendo cada línea números empezando en uno y acabando en el numero de la línea.
altura = 5
#altura = int(input("Introduce la altura de la escalera: "))

for i in range(altura):
    for j in range(altura):
        if j <= i:
            print(j+1, end=" ")
    print()