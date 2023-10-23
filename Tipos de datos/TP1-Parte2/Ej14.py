"""14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo 
que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables."""
#Ejercicio 14
A = int(input("Ingrese el primer numero: "))
B = int(input("Ingrese el segundo numero: "))
print(f"Variables A:{A}, B:{B}")

aux = A
A = B
B = aux
print(f"Variables intercambiadas A:{A}, B:{B}")