"""1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola 
que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años."""
#Ejercicio 1
"""computer_years = int(input("Ingrese los años de su computadora: "))

if computer_years <= 2:
    print("El coputador es nuevo.")
else:
    print("El computador es viejo.")"""
    
    
"""2- Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo."""
#Ejercicio 2
"""computer_years = int(input("Ingrese los años de su computadora: "))

if computer_years < 0:
    print("Error. Debe ingresar un numero positivo")
elif computer_years <= 2:
    print("El coputador es nuevo.")
else:
    print("El computador es viejo.")"""
    
    
"""3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
A continuación. Imprimir 'coincidencia' si ambos nombres comienzan con la misma letra. Si no es así, imprimir 
'no hay coincidencia'."""
#Ejercicio 3
"""name1 = input("Ingrese un nombre: ")
name2 = input("Ingrese otro nombre: ")

if name1[0].lower() == name2[0].lower():
    print("Coincidencia")
else:
    print("No hay coincidencia")"""
    
   
"""4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul. Según el 
candidato elegido (A, B o C) se debe imprimir el mensaje: 'Usted ha votado por el partido [color del candidato 
elegido]. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
indicar 'Opción errónea'."""
#Ejercicio 4
"""vote = input(f"Partidos: \nA : rojo \nB : verde \nC : azul \nIngrese su voto: ")

if vote == 'A':
    print(f"Usted ha votado por el partido rojo")
elif vote == 'B':
    print(f"Usted ha votado por el partido verde")
elif vote == 'C':
    print(f"Usted ha votado por el partido azul")"""
    
    
"""5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje 'Es vocal'. 
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle 
que no se puede procesar el dato."""
#Ejercicio 5
"""vowel = input("Ingrese una letra: ")
vowel_list = "aeiou"

count = vowel_list.count(vowel)

if len(vowel) > 1 :
    print("No se puede procesar el dato")
elif count == 1:
    print("Es vocal")
else:
    print("No es vocal")"""
    
    
"""6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser 
divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
#Ejercicio 6
"""leap_year = int(input("Ingrese un año: "))

if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print(f"El año {leap_year} es un año bisiesto")
else:
    print(f"El año {leap_year} no es un año bisiesto")"""
    
    
    
"""7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres."""
#Ejercicio 7
"""number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))

if number1 < number2 and number1 < number3:
    print(f"El numero {number1} es el menor")
elif number2 < number1 and number2 < number3:
    print(f"El numero {number2} es el menor")
elif number3 < number1 and number3 < number2:
    print(f"El numero {number3} es el menor")"""
    
    
"""8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es 
“Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede 
ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”."""
#Ejercicio 8
"""user_name = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")

if user_name == "Gwenevere" and password == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")"""
    
    
"""9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A 
está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
el grupo que le corresponde."""
#Ejercicio 9
"""name = input("Ingrese su nombre: ")
gender = input("Ingrese su sexo(femenino/masculino): ")

letters_name1 = "abcdefghijklm"
letters_name2 = "nñopqrstuvwxyz"

count1 = letters_name1.count(name[0].lower())
count2 = letters_name2.count(name[0].lower())

if count1 == 1 and gender.lower() == "femenino" or count2 and gender.lower() == "masculino":
    print("Corresponde al grupo A")

elif count2 == 1 and gender.lower() == "femenino" or count1 and gender.lower() == "masculino":
    print("Corresponde al grupo B")"""
    
    
"""10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular 
de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario 
la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000."""
#Ejercicio 10
"""age = int(input("Ingrese su edad: "))

if age < 4:
    print("Podes entrar gratis")
elif age >= 4 and age <= 18:
    print("Debes pagar $500")
elif age > 18:
    print("Debes pagar $1000")"""
    
    
"""11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes 
para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un 
ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por 
pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""
#Ejercicio 11
"""pizza_vegetarian = input("Pizzería Bella Napoli. \n¿Quiere una pizza vegetariana(si/no)?")

if pizza_vegetarian.lower() == "si":
    ingredient = input("• Ingredientes vegetarianos: Pimiento y tofu. \nElija un ingrediente: ")
elif pizza_vegetarian.lower() == "no":
    ingredient = input("• Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. \nElija un ingrediente: ")

print(f"La pizza elegida {pizza_vegetarian} es vegetariana \nIngredientes elejidos: mozzarella, tomate y {ingredient}")"""


"""12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado 
desde ese año o cuántos años faltan para llegar a ese año."""
#Ejercicio 12
"""actual_age = int(input("Ingrese el año actual: "))
age = int(input("Ingrese cualquier año: "))

if actual_age > age:
    print(f"Desde {age} hasta {actual_age} han pasado {actual_age - age} años")
else:
    print(f"Para llegar a {age} faltan {age - actual_age} años")"""
    
    
"""13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
Haciendo que el programa avise cuando se escriben valores negativos o nulos."""
#Ejercicio 13
"""number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

if number1 <= 0 or number2 <= 0:
    print("Error. Alguno de los numero ingresados es negativo o nulo")
elif number1 > number2:
    if number1 % number2 == 0:
        print(f"{number1} es multiplo de {number2}")
    else:
        print(f"{number1} no es multiplo de {number2}")
else:
    if number2 % number1 == 0:
        print(f"{number2} es multiplo de {number1}")
    else:
        print(f"{number2} no es multiplo de {number1}")"""
        
        
"""14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba 
la solución.Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o 
que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a"""
#Ejercicio 14
"""a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

if a == 0:
    if b == 0:
        print("La ecuación {a}x + {b} = 0 tiene infinitas soluciones.")
    else:
        print("La ecuación {a}x + {b} = 0 no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación {a}x + {b} = 0 es x = {x}")"""
    
    
"""15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un 
círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene 
que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de 
un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área."""
#Ejercicio 15
"""import math
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
    print(f"El area del circulo es {area}")"""
    
    
"""16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b"""
#Ejercicio 16
"""print("Calculadora")
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

print("Operaciones: \n1.Suma \n2.Multiplicacion \n3.Resta \n4.Division")
opc = int(input("Segun las opciones ingrese el numero de la operacion que desea realizar: "))

if opc == 1:
    operation = "suma"
    result = number1 + number2
elif opc == 2:
    operation = "multiplicacion"
    result = number1 * number2
elif opc == 3:
    operation = "resta"
    result = number1 - number2
elif opc == 4:
    operation = "division"
    result = number1 / number2
   
print(f"La {operation} entre {number1} y {number2} es {result}")"""


"""17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje 
diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de 
esos, imprimir otro mensaje."""
#Ejercicio 17
"""day = input("Ingrese un dia de la semana: ")

if day.lower() == "lunes":
    print("Es lunes. Arranca la semana")
elif day.lower() == "viernes":
    print("Es viernes. Ya casi es fin de semana")
elif day.lower() == "sabado" or day.lower() == "domingo":
    print("Ya es fin de semana")
elif day.lower() == "martes" or day.lower() == "miercoles" or day.lower() == "jueves":
    print("No es un día relevante de la semana.")"""
    
    
"""18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora. La jornada de trabajo 
mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas 
laborales comunes."""
#Ejercicio 18
"""hours = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salary_per_hour = int(input("Ingrese el salario por hora: "))
minimum_hous = 48
salary = hours * salary_per_hour

if hours > minimum_hous:
    extra_percentage = salary * 0.10
    salary += extra_percentage
    print(f"Trabajó horas extras, su salario es de ${salary}")
else:
    print(f"Su salario es de ${salary}")"""
    
    
"""19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe 
un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento."""
#Ejercicio 19
"""pencil = int(input("Ingrese la cantidad de lapices que quiere comprar: "))
price = pencil * 60

if pencil >= 1000:
    discount = price * 0.07
    price -= discount
else:
    price = price
    
print(f"Si compras {pencil} lapices el precio final es de ${price}")"""


"""20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) 
notas, es mayor o igual a 6; caso contrario saldrá desaprobado."""
#Ejercicio 20
"""sum = 0

for i in range(1,5):
    grade = int(input(f"Ingrese la {i}° notas del alumno: "))
    sum += grade

average = sum / 4
if average >= 6:
    print(f"El alumno está aprobado con promedio {average}")
else:
    print(f"El alumno está desaprobado con promedio {average}")"""