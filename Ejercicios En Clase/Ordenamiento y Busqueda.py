import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
#Ordenamiento y busqueda:
numbers_list = [91,55,7,3,14,1,6,12,7,2]
print("""------------------Menú------------------
1. Ordenamiento de burbuja(Bubble Sort)
2. Ordenamiento de selección(Selection Sort)
3. Ordenamiento de inserción(Insert Sort)
4. Combinar ordenamiento(Merge Sort)
5. Busqueda Lineal
6. Busqueda Binaria""")
option = int(input("Ingrese el numero de la opcion que quiere realizar: "))
    
if option == 1:
    #Ordenamiento de burbuja
    Funciones.bubble_sort(numbers_list)
    print("Ordenamiento de burbuja: ", end = "")    
    Funciones.show_list(numbers_list)
    
elif option == 2:
    #Ordenamiento de seleccion
    Funciones.selection_sort(numbers_list)
    print("Ordenamiento de selección: ", end = "")
    Funciones.show_list(numbers_list)
    
elif option == 3:
    #Ordenamiento de insercion
    Funciones.insert_sort(numbers_list)
    print("Ordenamiento de insercion: ", end = "")
    Funciones.show_list(numbers_list)
    
elif option == 4:
    #Combinar ordenamiento
    Funciones.merge_sort(numbers_list)
    print("Combinar ordenamiento: ", end = "")
    Funciones.show_list(numbers_list)
    
elif option == 5:
    #Busqueda Lineal
    Funciones.linear_search(numbers_list)
    
elif option == 6:
    #Busqueda Binaria
    Funciones.bubble_sort(numbers_list)
    Funciones.show_list(numbers_list)
    Funciones.binary_search(numbers_list)


