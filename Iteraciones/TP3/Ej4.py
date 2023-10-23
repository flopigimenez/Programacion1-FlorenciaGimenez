"""4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
cuenta atrás desde ese número hasta cero separados por comas."""
#Ejercicio 4
number = int(input("Ingrese un numero: "))

for i in range(number, 0-1, -1):
    print(i, end=", ")
    
