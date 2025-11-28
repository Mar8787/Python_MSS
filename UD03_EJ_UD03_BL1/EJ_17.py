# 16. Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario incorrecto

nombre = input("Introducza su nombre de usuario: ")
contrasenia = input("Introduzca su contraseña: ")

if  nombre != "Juan":
    print("Nombre de usuario incorrecto")
elif contrasenia != "1234":
    print("Contraseña incorreta")
else:
    print("Inicio de sesión correcto")