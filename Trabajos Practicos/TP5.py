import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
"""1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos."""
# Ejercicio 1
"""print("---- Bienvenido ----")
# Ingreso del numero de documento
dni = input("** Ingrese su numero de documento (DNI): ")
# Verificacion del numero de documento
valid_id = Funciones.dni_verification(dni)

if valid_id == True:
    print(f"* El numero de documento es válido ({valid_id})")
else:
    print(f"* El numero de documento no es válido ({valid_id})")"""

"""2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que 
las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del 
string pasado por parámetro."""
# Ejercicio 2
"""print("---- Bienvenido ----")
phrase = input("** Ingrese una palabra o frase: ")
word_list = phrase.split()

# Verificacion de longitud de la ultima palabra
last_word_length = Funciones.last_word_lenght(word_list)

print(f"La longitud de la palabra ingresada, o de la ultima palabra de la frase ingresada es {last_word_length}")"""

"""3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante 
el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo
caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un
bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de
letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
-Nombre: María Ines Rosales
-DNI: 25469648
-ID -> Maria7254"""
# Ejercicio 3
"""print("---- SISTEMA DE REGISTRO DE SOCIOS DEL CLUB ---- ")
print("- A continuación, se le pedirá ingresar los datos de los integrantes, para terminar, ingrese un nombre vacio") 

# Ingreso de los datos
print("\n*** DATOS DEL INTEGRANTE ***")
print("* Nombre: Utilice el siguiente formato: nombre, apellido.\n* En caso de tener 2 nombres, el formato es "
+ "el siguiente: primernombre, segundonombre, apellido.\n  Si tiene mas de un apellido, ingrese solo uno:")
while True:

    # Ingreso nombre
    member_name = input("Nombre: ")
    name_parts = member_name.split()

    if name_parts == []:
        # Si se ingresa un nombre vacío, el programa finaliza
        break
    else:
        # En caso de ingresar un nombre no vacio, verifico que siga el formato
        valid = Funciones.name_verification(name_parts)

        if valid:
            print(f"* DNI: Ingrese el dni del miembro {name_parts[0]} recuerde que el DNI es valido si tiene 7 u 8 numeros")
            while True:
                # Ingreso DNI
                member_dni = input("DNI: ")
                # Verifico que el dni sea valido
                valid_dni = Funciones.dni_verification(member_dni)
                if valid_dni:
                    # Genero e imprimo el ID del miembro
                    print("\n        ***** IDENTIFICADOR DE SOCIO GENERADO *****")
                    id = Funciones.member_id_generator(name_parts, member_dni)

                    print(f"NOMBRE: {name_parts[0].replace(',', '').strip().capitalize()} {name_parts[-1].capitalize()}")
                    print(f"DNI: {member_dni}")
                    print(f"ID: {id}")
                    print("\n*** Nuevo integrante ***")
                    break
                else:
                    print("--- DNI invalido, ingreselo nuevamente ---")
                    continue
        else:
            print("--- Nombre invalido, por favor ingreselo nuevamente siguiendo el formato solicitado")"""

"""4. Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.
Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""
#Ejercicio 4
"""#Declaro e inicializo las variables para posteriormente enviar como argumentos

num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))

Funciones.is_multiple(num1, num2)"""

"""5. Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de
cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir."""
#Ejercicio 5
"""days = int(input('Ingrese la cantidad de días que ingresará: '))

# Ya teniendo los días, recorro esa cantidad en un for y retorno la función en un variable promedio para posteriormente
# imprimirla

for i in range(1, days+1):
    print(f'Día {i}'.center(50, '-'))
    mx_temp = int(input('Ingrese la temperatura máxima: '))
    mn_temp = int(input('Ingrese la temperatura mínima: '))
    average = Funciones.avg_temperature(mx_temp, mn_temp)
    print(f'La temperatura promedio de este día fue: {average}')"""

""" 6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada
letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función."""
#Ejercicio 6
"""#Le pido al usuario la palabra a convertir, para posteriormente retornar el resultado de la función con dicho argumento
#En una variable nueva palabra

word = input('Ingrese una palabra: ')
new_word = Funciones.return_wh_spaces(word)

print(new_word)"""

"""7. Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
 Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior."""
#Ejercicio 7
"""numeros = []
for i in range(5):
    numero = input("Ingrese los numeros de la lista: ")
    numeros.append(numero)

print(Funciones.mayor_menor(numeros))"""

"""8. Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa 
principal que lea el radio de una circunferencia y muestre su área y perímetro."""
#Ejercicio 8
"""radio_elegido = int(input("Ingrese el radio de la circunferencia: "))
print(Funciones.circunferencia(radio_elegido))"""
 
"""9. Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve 
Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de 
intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor."""
#Ejercicio 9
"""intentos = 0
while(True):
    user = input("Ingrese el usuario: ")
    password= input("Ingrese la contraseña: ")
    if Funciones.login(user ,password, intentos):
           print("Ingreso correctamente")
           break
    else:
        intentos += 1
        print("intento numero: " + str(intentos))"""

"""10) Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un
diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los
productos del carrito y devolver el precio final de la compra"""
#Ejercicio 10
"""shopping_cart = {}
discounts = {}

while True:
    product = input("Ingrese el producto o fin para dejar de cargar productos: ")
    
    if product.lower() == "fin":
        break
        
    while True:
        prize = float(input("Ingrese el precio del producto: "))
        
        if prize >0: 
            shopping_cart[product] = prize
            break
        else:
            print("el precio no puede ser 0 o negativo")

while True:
    product = input("Ingrese el producto con descuento o fin para dejar de cargar descuentos: ")

    if product.lower() == "fin":
        break

    while True:
        num = float(input("Ingrese el porcentaje de descuento para el producto: "))
        if num >0: 
            discounts[product] = num
            break
        else:
            print("el descuento no puede ser 0 o negativo")

total_prize = Funciones.apply_discount(shopping_cart, discounts)
print(f"Precio total con descuento: {total_prize}")"""

"""11)Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de
aplicar la función dada a cada uno de los elementos de la lista."""
#Ejercicio 11
"""original_list = [1, 2, 3, 4, 5]

result = Funciones.apply_function_to_list(Funciones.square, original_list)
print(f"lista original {original_list}")
print(f"lista con los resultados de los numeros al cuadrado {result}")"""

"""12) Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y
su longitud."""
#Ejercicio 12
"""phrase="Pepito saludo a Juanito"

result = Funciones.word_length_dict(phrase)

print(result)"""

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
    
