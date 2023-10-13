""" 1- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""
#Ejercicio 1 
"""word = input("Ingrese una palabra: ")

for i in range(0,10):
    print(i+1, word)"""
    
""" 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años 
que ha cumplido (desde 1 hasta su edad)."""
#Ejercicio 2 
"""age = int(input("Ingrese su edad: "))

print("Años cumplidos: ")
for i in range(0,age):
    print(i+1)"""
    
"""3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas."""
#Ejercicio 3
"""number = int(input("Ingrese un numero: "))

print(f"Numeros impares desde 1 hasta {number}: ", end=" ")
for i in range(1, number+1):
    if i % 2 != 0:
        print(i, end=", ")"""
    
"""4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
cuenta atrás desde ese número hasta cero separados por comas."""
#Ejercicio 4
"""number = int(input("Ingrese un numero: "))

for i in range(number, 0-1, -1):
    print(i, end=", ")"""
    
"""5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

"""6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido."""


"""12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.""" 
#Ejercicio 12
"""phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
letter_found = 0

#entra a un bucle que sirve como contador para cuando se cumple la condición
for i in phrase:   
    if i == letter:
        letter_found += 1
    
print(f"La letra {letter} aparece {letter_found} veces en la frase")"""

"""13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba “salir” que terminará."""
#Ejercicio 13
"""entry = input("Ingrese una palabra o numero: ")

#entra a un bucle en el que se imprime lo que ingresa el usuario hasta que se deje de cumplir la condicion
while entry.lower() != "salir":
    print(entry)
    entry = input("Ingrese una palabra o numero, si quiere salir ingrese salir: ")"""

"""14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y 
cuáles impares desde el primero hasta el segundo."""
#Ejercicio 14
"""number1 = (int(input("Ingrese el primer numero: ")))
number2 = (int(input("Ingrese el segundo numero: ")))

#entra a un bucle en el que si la condicion es verdadera muestra los numeros pares
print(f"Numeros pares entre {number1} y {number2}: ", end= " ")
for i in range(number1,number2 +1):
    if i % 2 == 0:
        print(i, end=" ")

print(" ")
#entra a un bucle en el que si la condicion es verdadera muestra los numeros impares
print(f"Numeros impares entre {number1} y {number2}: ", end= " ")
for i in range(number1,number2+1):
    if i % 2 != 0:
        print(i, end=" ")

print(" ")"""
    
"""15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""
#Ejercicio 15
"""number = int(input("Ingrese un número entero mayor que cero: "))

#entra a un bucle en el que evalua la condicion t si es verdadera muetra los divisore del numero pedido al ususario
print(f"Los divisores de {number} son:", end= " ")
for i in range(1,number+1):
    if number % i == 0:
        print(i, end= " ")"""