"""1.	Calcular el perímetro y área de un rectángulo dada su base y su altura."""
#Ejercicio 1
"""base = 5
height = 15

perimeter = 2* (base + height)
area = base * height

print(f"El perimetro de un rectangulo de base {base} y de altura {height} es {perimrter}")
print(f"El area de un rectangulo de base {base} y de altura {heigth} es {area}")"""

"""2.  Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
#Eercicio 2
"""leg1 = 3
leg2 = 4

hypotenuse = (leg1**2 + leg2**2) ** (1/2)
print(f"La hipotenusa de un triangulo rectangulo de catetos {leg1} y {leg2} es {hypotenuse}")"""

"""3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos."""
#Ejercicio 3
"""number1 = 7
number2 = 4

print(f"Suma entre {number1} y {number2}: ", number1 + number2)
print(f"Resta entre {number1} y {number2}: ", number1 - number2)
print(f"Multiplicacion entre {number1} y {number2}: ", number1 * number2)
print(f"Division entre {number1} y {number2}: ", number1 / number2)"""

"""4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. 
Recordar que la fórmula para la conversión es: c=(f-32)*5/9"""
#Ejercicio 4
"""degrees_Fahrenheit = 30
degrees_Celsius = (degrees_Fahrenheit - 32)*5/9
print(f"{degrees_Fahrenheit} grados Fahrenheit son {degrees_Celsius} grados Celsius")"""
 
"""5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)
c)	edad = int(input(“Edad: “))
print(tu edad es, edad)
d)	edad = int(input(“Edad: “))
print(“Veamos si tu edad es 18…”, edad=18)"""
#Ejemplo 5
"""#a)
nombre = input("Ingresed su nombre: ")
A = input(f"{nombre}, ¿Cuál es tu canción favorita?: ")
print(A)"""

"""#b)
precio = int(input("Precio: "))
total = precio + (precio * 0.1)
print(total)"""

"""#c)
edad = int(input("Edad: "))
print(f"Tu edad es, {edad}")"""

"""#d)
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad==18)"""

"""6.	Calcular la media de tres números pedidos por teclado."""
#Ejercicio 6
"""number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))

average = (number1 + number2 + number3) / 3
print(f"La media es {average}")"""

"""7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas 
y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos."""
#Ejercicio 7
"""minutes = int(input("Ingrese los segundos: "))
hours = int(minutes / 60)
min = minutes % 60

print(f"{minutes} minutos son {hours} horas y {min} minutos.")"""

"""8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor 
desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones."""
#Ejercicio 8
"""base_salary = float(input("Ingrese el salario base: "))

sale1 = float(input("Ingrese el monto de la primera venta: "))
sale2 = float(input("Ingrese el monto de la segunda venta: "))
sale3 = float(input("Ingrese el monto de la tercera venta: "))

commission = (sale1 + sale2 + sale3) * 0.10
total_money = base_salary + commission

print(f"El monto total de comisión es: {commission}")
print(f"El salario total que recibirá en el mes es: {total_money}")"""

"""9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
cuanto deberá pagar finalmente por su compra."""
#Ejercicio 9
"""buy_price = float(input("Ingrese el precio de la compra: "))

percentage = buy_price * 0.15
total_price = buy_price - percentage

print(f"Con el descuento el cliente deberá pagar por su compra ${total_price}")"""

"""10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha 
calificación se compone de los siguientes porcentajes:
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final."""
#Ejercicio 10
"""partial_grade1 = float(input("Ingrese la nota de su primer parcial: "))
partial_grade2 = float(input("Ingrese la nota de su segundo parcial: "))
partial_grade3 = float(input("Ingrese la nota de su tercero parcial: "))
parcial_grade = (partial_grade1 + partial_grade2 + partial_grade3) / 3
parcial_grade *= 0.55

final_exam = float(input("Ingrese la nota de su examen final: "))
final_exam *= 0.30

final_work = float(input("Ingrese la nota de su trabajo final: "))
final_work *= 0.15

final_grade = (parcial_grade + final_exam + final_work) 
print(f"La calificación final del alumno en la materia de Algoritmos es un {final_grade}")"""

"""11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su 
diferencia, de modo que el resultado sea siempre positivo)."""
#Ejercicio 11
"""number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

diference = abs(number1 - number2)

print(f"La diferencia ente {number1} y {number2} es {diference}")"""

"""12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica."""
#Ejercicio 12
"""number = int(input("Ingrese un numero: "))

print(f"La raíz cuadrada de {number} es {number**2}")
print(f"La raíz cúbica de {number} es {number**3}")"""

"""13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
Ejemplo, si se introduce 23 que muestre 32."""
#Ejercicio 13
"""number = int(input("Ingrese un numero de dos cifras: "))

if number > 9 and number < 100:    
    number1 = number % 10
    number1 *= 10

    number2 = number // 10
    
    if number1 == 0:
        number1 = str(number1)
        number2 = str(number2)
        print(f"El número {number} invertido es {number1 + number2}")
    else:
        print(f"El número {number} invertido es {number1 + number2}")
else:
    print("El número no es de dos cifras")"""

"""14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo 
que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables."""
#Ejercicio 14
"""A = int(input("Ingrese el primer numero: "))
B = int(input("Ingrese el segundo numero: "))
print(f"Variables A:{A}, B:{B}")

aux = A
A = B
B = aux
print(f"Variables intercambiadas A:{A}, B:{B}")"""

"""15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta 
llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B."""
#Ejercicio 15
"""leaving_time = input("Ingrese el horario de partida de la cuidad A en formato HH:MM:SS: ")

T = int(input("Ingrese el tiempo de viaje en segundos: "))

arrival_time = int(leaving_time[0:2]) * 3600 + int(leaving_time[3:5]) * 60 + int(leaving_time[6:8]) + T

HH = arrival_time // 3600
MM = (arrival_time % 3600) // 60
SS = arrival_time % 60

print(f"La hora de llegada a la ciudad B es {HH}:{MM}:{SS}")"""

"""16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales."""
#Ejercicio 16
"""name = input("Ingrese su nombre: ")
surname1 = input("Ingrese su primer apellido: ")
surname2 = input("Ingrese su segundo apellido: ")

print(f"Iniciales: {name[0]}, {surname1[0]}, {surname2[0]}")"""

"""17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada 
usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”."""
#Ejercicio 17
"""usuario = input("Ingrese su nombre: ")
print(f"Ahora estás en la matrix, {usuario}.")"""

"""18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, 
sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar."""
#Ejercicio 18
"""dinner_cost = int(input("Ingrese cuanto costó la cena: "))
final_cost = dinner_cost + (dinner_cost * 0.062) + (dinner_cost * 0.10)
print(f"El monto final a pagar es {final_cost}")"""

"""19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos 
en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato 
dd/mm/aaaa."""
#Ejercicio 19
"""day = int(input("Ingrese el dia de su nacimiento: "))
month = int(input("Ingrese el mes de su nacimiento: "))
year = int(input("Ingrese el año de su nacimiento: "))

print(f"Fecha de nacimiento {day}/{month}/{year}")"""

"""20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA."""
#Ejercicio 20
"""day = int(input("Ingrese el dia de su nacimiento: "))
month = int(input("Ingrese el mes de su nacimiento: "))
year = int(input("Ingrese el año de su nacimiento: "))

DDMMAA = str(day) + "/" + str(month) + "/" + str(year)
print(f"Fecha de nacimiento {DDMMAA}")"""

"""21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para 
saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad 
(en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible 
necesarios."""
#Ejercicio 21
"""km = int(input("Ingrese cuántos kilómetros puede recorrer su moto con 1 litro de combustible: "))
l = int(input("Ingrese la capacidad (en litros) que tiene el tanque: "))
total_km = int(input(" Ingrese cuántos kilómetros en total recorrerán: "))

tanks = total_km / (km * l)

print(f"La cantidad de tanques de combustible necesarios son {tanks}")"""
