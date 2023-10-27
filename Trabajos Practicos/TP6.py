import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
"""1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario 
debe ingresar 0, el cual no debe guardarse."""
"""2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su 
primera ocurrencia. Mostrar un mensaje si no es posible eliminar."""
"""3.	Imprimir la sumatoria de todos los números de la lista."""
"""4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores 
que el número dado. Imprimir esta nueva lista, iterando por ella."""
"""#Ejercicio 1
list_numbers = []
number = 1
while number != 0:
    number = int(input("Ingrese un numero para llenar la lista. para salir ingrese 0: "))
    if number != 0:
        list_numbers.append(number)

print("Lista: ", end = "")
Funciones.show_list(list_numbers)

#Ejercicio 2
print("-----------------------------------------")
number_to_delet = int(input("Ingrese un numero: "))

if number_to_delet in list_numbers:
    list_numbers.remove(number_to_delet)
    print(f"Se elimino la primera ocurrencia del numero {number_to_delet}")
else:
    print(f"El numero {number_to_delet} no se puede eliminar, no se encuentra en la lista")

print("Lista: ", end = "")
Funciones.show_list(list_numbers)

#Ejercicio 3
print("-----------------------------------------")
sum = 0

for i in list_numbers:
    sum += i

print(f"La suma de los numero de la lista es {sum}")   
    
#Ejercicio 4
print("-----------------------------------------")
number_to_compare = int(input("Ingres un numero: "))
new_list = []

for i in list_numbers:
    if i < number_to_compare:
        new_list.append(i)

print("Lista: ", end = "")    
Funciones.show_list(new_list)"""