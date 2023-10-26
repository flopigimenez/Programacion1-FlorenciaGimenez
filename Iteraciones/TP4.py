"""1. Create a while loop with the following characteristics:
• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was
skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the 
loop was broken when x was ' + x.
• The console output should look like this: (IMAGEN)"""
#Ejercicio 1
"""x = 0
while x < 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print(f"Se saltó el valor {x} de x")
    elif x == 15:
        break
    else:
        print(x)
        
print(f"Se rompió la ejecución del bucle cuando x valía: {x}")"""


"""1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en 
mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas."""
#Ejercicio 1
"""lines = []

while True:
    line = input("Ingrese una linea o deje en blanco para finalizar: ")
    if line:
        lines.append(line)
    else:
        break

for line in lines:
    print(line.upper())"""

"""2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350""" 
#Ejercicio 2
"""print("Operaciones: \nIngresar D para depositar dinero \nIngrese R para retirar dinero")
amount_d = 0
amount_r = 0

while True:
    operation = input("--> ") 
    
    if operation.upper() == "D":
        amount = int(input("D "))
        amount_d += amount
    elif operation.upper() == "R":
        amount = int(input("R "))
        amount_r += amount
    else:
        break

print("Saldo final: ", amount_d - amount_r)"""

"""3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo 
y el 1."""
#Ejercicio 3
"""number = 1
prime_numbers = 0

while number != 0:
    number = int(input("Ingrese un numero mayor a 1, para finalizar ingrese 0: "))
    
    if number <= 1 and number != 0:
        print("Numero incorrecto")
        continue
    
    count = 0
    
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            
    if count == 2:
        prime_numbers += 1  

print(f"Dentro de los numero ingresados hay {prime_numbers} numeros primos")"""

"""4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese 
rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que 
también sea divisible por 400."""
#Ejercicio 4
"""a = int(input("Ingrese un año: "))
b = int(input("Ingrese otro año: "))

if a < b:
    year1 = a
    year2 = b
else:
    year1 = b
    year2 = a
    
for i in range(year1, year2):
    if (i % 4 == 0 and i % 100 != 0 or i % 400 == 0) and i % 10 == 0:
        print(f"El año {i} es un año bisiesto y multiplo de 10")
    else:
        continue"""

"""5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza 
la declaración continue para omitir los números impares."""
#Ejercicio 5
"""for i in range(1, 21):
    if i % 2 == 0:
        print(i, end = " ")
    else:
        continue"""

"""6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres 
el número, usa break para salir del bucle."""
#Ejercicio 6
"""number_list = [1, 7, 8, 19, 3, 4, 10, 54, 2, 5]
number = int(input("Ingrese un numero para buscar en la lista: "))

for i in number_list:
    if number == i:
        print(f"El numero {number} si se encuntra en la lista")
        break    
    
else:
    print(f"El numero {number} no se encuntra en la lista")"""

"""7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle 
while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir 
del bucle (Mostrar un mensaje por cada opción elegida)."""
#Ejercicio 7
"""print("Menu \n1. Opcion 1 \n2. Opcion 2 \n3. Opcion 3")
while True:
    
    option = int(input("- "))
    
    if option == 0:
        break
    elif option == 1:
        print("Elegiste la opcion 1")
    elif option == 2:
        print("Elegiste la opcion 2")
    elif option == 3:
        print("Elegiste la opcion 3")"""