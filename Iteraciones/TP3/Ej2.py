""" 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años 
que ha cumplido (desde 1 hasta su edad)."""
#Ejercicio 2 
age = int(input("Ingrese su edad: "))

print("Años cumplidos: ")
for i in range(0,age):
    print(i+1)
    
