"""10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha 
calificación se compone de los siguientes porcentajes:
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final."""
#Ejercicio 10
partial_grade1 = float(input("Ingrese la nota de su primer parcial: "))
partial_grade2 = float(input("Ingrese la nota de su segundo parcial: "))
partial_grade3 = float(input("Ingrese la nota de su tercero parcial: "))
parcial_grade = (partial_grade1 + partial_grade2 + partial_grade3) / 3
parcial_grade *= 0.55

final_exam = float(input("Ingrese la nota de su examen final: "))
final_exam *= 0.30

final_work = float(input("Ingrese la nota de su trabajo final: "))
final_work *= 0.15

final_grade = (parcial_grade + final_exam + final_work) 
print(f"La calificación final del alumno en la materia de Algoritmos es un {final_grade}")