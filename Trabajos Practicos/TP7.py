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

"""3. Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro 
(título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en 
función de un campo específico, como el año de publicación o el autor."""
#Ejercicio 3
"""# Lista con diccionarios, cada diccionario contiene informacion sobre X libro
dictionary_list =  [
    {"name": "El código Da Vinci", "author": "Dan Brown", "year": 2003},
    {"name": "El gran Gatsby", "author": "Francis Scott Key Fitzgerald " ,"year": 1925},
    {"name": "El niño con el pijama de rayas", "author": "John Boyne", "year": 2006},
    {"name": "La naranja mecánica", "author": "Anthony Burgess", "year": 1962},
    {"name": "Cien años de soledad", "author": "Gabriel García Marquéz", "year": 1967},
    {"name": "Crimen y castigo", "author": "Fyodor Dostoevsky", "year": 1866}]
# Muestro los libros disponibles
print("------------ Libros disponibles ------------")
for book in dictionary_list:
    print(f"- {book['name']}, ({book['year']}) de {book['author']}")

# Pregunto al usuario como desea ordenarlos
while True:
    option = int(input(
        "\n1) Ordenar alfabeticamente en funcion del nombre del autor. \n2) Ordenar en funcion del año de publicacion. \n3) Salir\n"))

    if (option < 1) or (option > 3):
        print("Ingrese una opcion válida")
    else:
        # Si ingreso 1 se ordena por en funcion del nombre del autor
        if option == 1:
            dictionary_list = Funciones.bubble_sort_3(dictionary_list, "author")
            print("\n")
            for book in dictionary_list:
                print(f"- {book['author']}: {book['name']}, ({book['year']})")

        # Si ingreso 2 se ordena por año de publicacion
        elif option == 2:
            dictionary_list = Funciones.bubble_sort_3(dictionary_list, "year")
            print("\n")
            for book in dictionary_list:
                print(f"- {book['year']}: {book['name']}, de {book['author']}")
        # Si ingreso 3 el programa finaliza
        elif option == 3:
            break"""
 
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

"""6. Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de 
ordenamiento por conteo."""
#Ejercicio 6
"""list_num = [1,4,5,2,10,23,0]
print("Lista: " + str(list_num))
lista_ordenada = Funciones.count_sort(list_num)
print("Lista ordenada: " + str(lista_ordenada))"""

"""7. Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta 
lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres 
ordenadas alfabéticamente."""
#Ejercicio 7
"""lista_variada = [1, "Hola", "chau", 3, "Sol", 22, "Mar"]
print("Lista: " + str(lista_variada))
lista_str = []
lista_int = []
for valores in lista_variada:
    if isinstance(valores, str):
        lista_str.append(valores)
    elif isinstance(valores, int):
        lista_int.append(valores)
Funciones.selection_sort(lista_str)
Funciones.bubble_sort(lista_int)
lista_final = lista_str + lista_int
print("Lista ordenada: " + str(lista_final))"""

"""8. Implementa el algoritmo de ordenamiento  Merge Sort y úsalo para ordenar una lista de números."""
#Ejercicio 8
"""list_of_numbers = [1,4,2,6,5,24]
print("Lista inicial: " + str(list_of_numbers))
Funciones.merge_sort(list_of_numbers)
print("lista ordenada: " + str(list_of_numbers))"""
