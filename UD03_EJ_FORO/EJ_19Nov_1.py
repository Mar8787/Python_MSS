#Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.

altura = int(input("Introduce el valor de la altura de la figura: "))

for i in range(0, (altura * 2) - 1):
    for j in range(0, (altura * 2) - 1):
        if i == ((altura * 2) - 1)-1 or j == ((altura * 2) - 1)-1 or i == 0 or j == 0 or i == j // 2 - 1 :
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print("")