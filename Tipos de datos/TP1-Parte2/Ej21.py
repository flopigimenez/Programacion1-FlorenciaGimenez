"""21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para 
saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad 
(en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible 
necesarios."""
#Ejercicio 21
km = int(input("Ingrese cuántos kilómetros puede recorrer su moto con 1 litro de combustible: "))
l = int(input("Ingrese la capacidad (en litros) que tiene el tanque: "))
total_km = int(input(" Ingrese cuántos kilómetros en total recorrerán: "))

tanks = total_km / (km * l)

print(f"La cantidad de tanques de combustible necesarios son {tanks}")