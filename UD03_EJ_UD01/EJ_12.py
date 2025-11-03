#* Ejericio 12. Dibuja un ordinograma de un programa que muestre los números pares comprendidos entre el 1 y el 200. Esta vez utiliza un contador sumando de 1 en 1.

for i in range(1, 201):
    resto = i % 2
    if resto == 0:
        print(i)