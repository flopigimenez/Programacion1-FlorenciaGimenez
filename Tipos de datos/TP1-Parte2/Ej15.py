"""15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta 
llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B."""
#Ejercicio 15
leaving_time = input("Ingrese el horario de partida de la cuidad A en formato HH:MM:SS: ")

T = int(input("Ingrese el tiempo de viaje en segundos: "))

arrival_time = int(leaving_time[0:2]) * 3600 + int(leaving_time[3:5]) * 60 + int(leaving_time[6:8]) + T

HH = arrival_time // 3600
MM = (arrival_time % 3600) // 60
SS = arrival_time % 60

print(f"La hora de llegada a la ciudad B es {HH}:{MM}:{SS}")