import Funciones
"""13.	Escribir una función que calcule el módulo de un vector. 
|m| = √(a^2 + b^2 + c^2)"""
#Ejercicio 13
"""a = int(input("Ingrese un numero para el primer componente: "))
b = int(input("Ingrese un numero para el segundo componente: "))
c = int(input("Ingrese un numero para el tercer componente: "))

Funciones.vector_magnitude(a,b,c)"""

"""14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función 
booleana que lo decida."""
#Ejercicio 14
"""number = int(input("Ingrese un numero: "))

print(f"El numero {number} es primo? {Funciones.prime_number(number)}")"""

"""15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la 
cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario."""  
#Ejercicio 15
"""number_list = []
amount_numbers = 0

while True:
    number = int(input(f"Ingrese un numero: "))
    if number <= 0:
        break
    else:
        number_list.append(number)
        amount_numbers += 1

for n in number_list:
    Funciones.factorial(n)
    
print(f"La cantidad de numeros leidos en total es de {amount_numbers} numeros")"""
    
