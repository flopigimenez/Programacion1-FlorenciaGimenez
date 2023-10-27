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
#Ejercicio 5
"""amount = int(input("Ingrese la cantidad a invertir: "))
interest = input("Ingrese el interés anual: ") 
years = int(input("Ingrese el número de años: "))

interest = float(interest.strip('%')) / 100 

for i in range(1, years+1):
    amount += amount * interest
    print(f"Capital obtenido el año {i}: ${amount}")"""

"""6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido."""
#Ejercicio 6
"""number = int(input("Ingrese un numero: "))

for i in range(1, number+1):
    print('*' * i)"""  

"""7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10."""
#Ejercicio 7
"""for i in range(1, 11):
    print("-----------")
    print(f"Tabla del {i}: ")
    for x in range(1, 11):
        print(f"{i} x {x} = {i*x}")"""

"""8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo."""
#Ejercicio 8
"""number = int(input("Ingrese un numero: "))

for i in range(1, number+1):
    for j in range(i*2-1, 0, -2):
        print(j, end = "")
    print("")"""

"""9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
usuario por la contraseña hasta que introduzca la contraseña correcta."""
#Ejercicio 9
"""password = input("Ingrese la contraseña: ")

while password.lower() != "contraseña":
    password = input("Contraseña incorrecta, intente de nuevo: ")
    
print("Contraseña correcta")"""
    
"""10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número 
primo o no."""
#Ejercicio 10
"""number = int(input("Ingrese un numero: "))
i = number
count = 0

while i != 0:
    if number % i == 0:
        count += 1
    i -= 1    

if count == 2:
    print(f"El numero {number} es primo")
else:
    print(f"El numero {number} no es primo")"""
    
"""11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
letras de la palabra introducida empezando por la última."""
#Ejercicio 11
"""word = input("Ingrese una palabra: ")

for i in word[::-1]:
    print(i)"""

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
        
        
"""16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba 
cuántos negativos ha introducido."""
#Ejarcicio 16
"""amount_numbers = int(input("Ingrese la cantidad de numeros que quiere introducir: "))
negative = 0

for i in range(1, amount_numbers+1):
    number = int(input(f"Ingrese el {i}° numero: "))
    if number < 0:
        negative += 1    

print(f"Ingresó {negative} números negativos")"""

"""17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en 
esa frase (sin repetirlas)."""
#Ejercicio 17
""" sentence = input("Ingrese una frase: ")
vowels = "aeiou"

print(f"Las vocales que aparecen en la frase son: ", end = "")
for i in vowels:
    if sentence.find(i) != -1:
        print(i, end = " ")"""

"""18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza 
con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la 
secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""
#Ejercicio 18
"""print("Los primeros 10 numeros de la sucesion de Fibonacci son: ")
i = 0
j = 1
print(i)
print(j)

for a in range(8):
    x = i + j
    print(x)
    i = j
    j = x"""

"""19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la 
cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades 
que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar 
que las cantidades ingresadas sean positivas."""
#Ejercicio 19
"""amount_to_save = int(input("Ingrese la cantidad de dinero que quiere ahorrar: "))
mony = 0
amount_saved = 0


while amount_saved < amount_to_save:
    mony = int(input("Ingrese la cantidad ahorrada que quiera guardar en la alcancía: "))
    
    if mony < 0:
        print("Ingrese una cantidad positiva")
    else:
        amount_saved += mony
    
print(f"Cantidad a ahorrar: {amount_to_save} \nCantidad ahorrada: {amount_saved}")        
print("Felicidades! Alcanzó la cantidad que queria ahorrar")"""

"""20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de 
todos los números ingresados."""
#Ejercicio 20
"""number = 1
sum = 0

while number != 0:
    number = int(input("Ingrese un numero. Para salir ingrese 0: "))
    sum += number

print(f"La suma de los numero ingresados es {sum}")"""

"""21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor 
número ingresado."""
#Ejercicio 21
""" number = 1
bigger_number = 0

while number != 0:
    number = int(input("Ingrese un numero. Para salir ingrese 0: "))
    if number > bigger_number:
        bigger_number = number

print(f"El mayor numero ingresados es {bigger_number}")"""

"""22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los 
dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos 
de los números ingresados por el usuario fueron números pares."""
#Ejercicio 22
"""number = 0
pair_numbers = 0

number = int(input("Ingrese un numero. Para salir ingrese -1: "))
while number != -1:
    sum = 0
    
    if number % 2 == 0:
        pair_numbers += 1
        
    while number != 0:
        digit = number % 10
        number //= 10
        sum += digit 
    print(f"La suma de sus digitos es: {sum}")
    
    number = int(input("Ingrese un numero. Para salir ingrese -1: "))
    
print(f"La cantidad de numeros pares ingresados es: {pair_numbers}")"""

"""23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce 
la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos 
cuando el usuario ingrese el monto 0."""
"""24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al 
finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
se le debe aplicar un 10% de descuento."""
#Ejercicio 23 y 24
"""number = 1
total = 0
i = 1

while number != 0:
    number = int(input(f"Ingrese el monto de la {i}° compra. Para salir ingrese 0: "))
    
    if number < 0:
        print("Ingrese una cantidad positiva")
    else:
        total += number
        i += 1

if total > 1000:
    print(" ")
    print ("El monto total supera los $1000, por lo que se le aplica un descuento del 10% ")
    discount = total - total * 0.10
    print(f"El monto total es: ${total} y con descuento es: ${discount}")
else:
    print(" ")
    print ("El monto total no supera los 1000$, no se le aplica el descuento")
    print(f"El monto total es: ${total}")"""
    
"""25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando 
todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1."""
#Ejercicio 25
"""number = int(input("Ingrese un numero: "))
factorial = 1

for i in range(1, number+1):
    factorial *= i
    
print(f"El factorial de {number} es {factorial}")"""