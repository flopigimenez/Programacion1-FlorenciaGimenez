import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
"""1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando 
el método de ordenamiento de burbuja."""
#Ejercicio 1
"""numbers_list = [91,55,7,3,14,1,6,12,7,2]
exchange = True

while exchange == True:
    exchange = False
    for i in range(1, len(numbers_list)):
        if numbers_list[i-1] > numbers_list[i]:
            aux = numbers_list[i-1]
            numbers_list[i-1] = numbers_list[i]
            numbers_list[i] = aux
            exchange = True

print("Lista: ", end = "")
Funciones.show_list(numbers_list)"""

"""2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden 
ascendente utilizando el método de ordenamiento de selección."""
#Ejercicio 2
"""letters_list = ['r', 'h', 'y', 'e', 'a', 'b', 'm']

for i in range(0, len(letters_list)): 
    smallest = i 
    for j in range(i+1, len(letters_list)):
        if letters_list[j] < letters_list[smallest]:
            smallest = j
    aux = letters_list[i]
    letters_list[i] = letters_list[smallest]
    letters_list[smallest] = aux    

print("Lista: ", end = "")
Funciones.show_list(letters_list)"""

 
"""4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su 
longitud. Puedes utilizar el método de ordenamiento de inserción."""
#Ejercicio 4
"""strings_list = ['manzana', 'banana', 'cereza', 'uva', 'pera']

for i in range(1, len(strings_list)):
    current_string = strings_list[i]
    j = i - 1
    while j >= 0 and len(strings_list[j]) > len(current_string):
        strings_list[j+1] = strings_list[j]
        j -= 1
    strings_list[j+1] = current_string

print("Lista: ", end = "")
Funciones.show_list(strings_list)"""

"""5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en 
lugar de ascendente."""
#Ejercicio 5
"""numbers_list = [91,55,7,3,14,1,6,12,7,2]
exchange = True

while exchange == True:
    exchange = False
    for i in range(1, len(numbers_list)):
        if numbers_list[i-1] < numbers_list[i]:
            aux = numbers_list[i-1]
            numbers_list[i-1] = numbers_list[i]
            numbers_list[i] = aux
            exchange = True

print("Lista: ", end = "")
Funciones.show_list(numbers_list)"""
