# 10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# • 55% del promedio de sus tres calificaciones parciales.
# • 30% de la calificación del examen final.
# • 15% de la calificación de un trabajo final.

parcial1 = 5.5
parcial2 = 10
parcial3 = 7.70
examen = 6.45
trabajo = 9.5
calificacionFinal = 0.00

parciales = (parcial1 + parcial2 + parcial3 ) / 3
calificacionFinal = parciales * 0.55 + examen * 0.30 + trabajo * 0.15

print(f"Nota final: {calificacionFinal:.2f}")
