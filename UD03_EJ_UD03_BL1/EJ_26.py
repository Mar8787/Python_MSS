# 26. En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
# Si los tres dados son seis, mostrar el mensaje “Excelente”
# Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
# Si un dado se obtiene seis, mostrar el mensaje “Regular”
# Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
# (Use el control switch).

print("Bienvenidos al Casino Puerto\n")
dado1 = int(input("Introduzca el valor del primer dado: "))
dado2 = int(input("Introduzca el valor del segundo dado: "))
dado3 = int(input("Introduzca el valor del tercer dado: "))

lista = [dado1, dado2, dado3]
cuantos6 = lista.count(6)

match cuantos6:
    case 3:
        print("Excelente")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")