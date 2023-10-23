"""15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un 
círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene 
que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de 
un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área."""
#Ejercicio 15
import math
print("Ingrese 'T' o 't' para calcular el area de un tiangulo \nIngrese 'C' o 'c' para calcular el area de un circulo")
area_toc = input("--> ")

if area_toc.lower() == 't':
    base =  int(input("Ingrese la base del triangulo: "))
    height = int(input("Ingrese la altura del triangulo: "))
    area = (base * height) / 2
    print(f"El area del triangulo es {area}")
elif area_toc.lower() == 'c':
    radius = int(input("Ingrese el radio del circulo: "))
    pi = math.pi
    area = (pi * radius ** 2)
    print(f"El area del circulo es {area}")