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

"""5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
 Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]"""

"""list_for_tuple = []
for number in new_list:
   numero = new_list.count(number)
   new_tuple = (number,numero)
   list_for_tuple.append(new_tuple)

unique_tuples = []
for number in set(new_list):
    count = new_list.count(number)
    unique_tuples.append((number, count))

print(unique_tuples)"""

"""6. Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, 
solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
a. Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b. Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c. Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""

"""students_primary = []
students_secondary = []
while(True):
    student_p = input("Ingrese el nombre de pila de los estudiantes de nivel primario, cuando quiera salir ingrese X: ")
    if student_p == "x":
        break
    else:
        students_primary.append(student_p)
while(True):
    student_s = input("Ingrese el nombre de pila de los estudiantes de nivel secundario, cuando quiera salir ingrese X: ")
    if student_s == "x":
        break
    else:
        students_secondary.append(student_s)
all_students =students_primary + students_secondary
unique_students = list(set(all_students))
print("Nombres de todos los alumnos de nivel primario y secundario (sin repeticiones):")
print(unique_students)
duplicates = [name for name in unique_students if all_students.count(name) > 1]
print("Nombres que se repiten entre los alumnos de nivel primario y secundario:")
print(duplicates)

unique_primary = list(set(students_primary))
unique_secondary = list(set(students_secondary))
names_unique_to_primary = [name for name in unique_primary if name not in unique_secondary]
print("Nombres de nivel primario que no se repiten en los de nivel secundario:")
print(names_unique_to_primary)

"""