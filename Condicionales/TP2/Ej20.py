"""20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) 
notas, es mayor o igual a 6; caso contrario saldrá desaprobado."""
#Ejercicio 20
sum = 0

for i in range(1,5):
    grade = int(input(f"Ingrese la {i}° notas del alumno: "))
    sum += grade

average = sum / 4
if average >= 6:
    print(f"El alumno está aprobado con promedio {average}")
else:
    print(f"El alumno está desaprobado con promedio {average}")