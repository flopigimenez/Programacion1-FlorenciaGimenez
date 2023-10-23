"""3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas."""
#Ejercicio 3
number = int(input("Ingrese un numero: "))

print(f"Numeros impares desde 1 hasta {number}: ", end=" ")
for i in range(1, number+1):
    if i % 2 != 0:
        print(i, end=", ")
    
