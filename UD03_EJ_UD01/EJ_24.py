#* Crea un programa que calcule y escriba la suma y el producto de los 10 primeros números naturales, partiendo de un numero que te den.

num = int(input("Introduce un número natural: "))
suma = 0
producto = 1
if num < 0:
    print("El número debe ser natural (mayor o igual a 0).")
else:
    for i in range(num, num + 10):
        suma += i
        producto *= i
    print(f"La suma de los 10 primeros números naturales a partir de {num} es: {suma}")
    print(f"El producto de los 10 primeros números naturales a partir de {num} es: {producto}")