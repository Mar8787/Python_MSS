# Crea un programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de 5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad

dinero = int(input("Introduce una cantidad de dinero en múltiplos de 5: "))
billetes5 = 0
billetes10 = 0
billetes20 = 0
billetes50 = 0
billetes100 = 0
billetes200 = 0
billetes500 = 0

if dinero >= 500:
    billetes500 = dinero // 500
    dinero = dinero % 500

if dinero >= 200:
    billetes200 = dinero // 200
    dinero = dinero % 200

if dinero >= 100:
    billetes100 = dinero // 100
    dinero = dinero % 100

if dinero >= 50:
    billetes50 = dinero // 50
    dinero = dinero % 50

if dinero >= 20:
    billetes20 = dinero // 20
    dinero = dinero % 20

if dinero >= 10:
    billetes10 = dinero // 10
    dinero = dinero % 10

if dinero >= 5:
    billetes5 = dinero // 5
    dinero = dinero % 5

# Los print de los billeres que se usan
if billetes500 > 0:
    print(f"Billetes de 500 = {billetes500}")

if billetes200 > 0:
    print(f"Billetes de 200 = {billetes200}")

if billetes100 > 0:
    print(f"Billetes de 100 = {billetes100}")

if billetes50 > 0:
    print(f"Billetes de 50 = {billetes50}")

if billetes20 > 0:
    print(f"Billetes de 20 = {billetes20}")

if billetes10 > 0:
    print(f"Billetes de 10 = {billetes10}")

if billetes5 > 0:
    print(f"Billetes de 5 = {billetes5}")