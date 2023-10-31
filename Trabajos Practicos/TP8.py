import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
#import Funciones
"""1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene."""
#Ejercicio 1
"""number = int(input("Ingrese un numero positivo: "))

while number < 0:
    number = int(input("Ingresó in numero invalido. Ingrese un numero positivo: "))

digits = Funciones.digits(number)

print(f"El numero {number} tiene {digits} digitos")"""

"""2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b."""
#Ejercicio 2
"""while True:
    n = int(input("Ingrese un numero entero: "))
    b = int(input("Ingrese otro numero entero: "))
    
    if n  <= 0 or b  <= 0:
        print("Alguno de los numeros ingresados es invalido. ")
    else:
        break
    
n_power_b = Funciones.power_of_b(n,b)

print(n_power_b)"""
#Ejercicio 3
"""3. Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a"""
"""def find_positions_recursive(a, b, start=0, positions=None):
    if positions is None:
        positions = []
    index = a.find(b, start)
    if index == -1:
        return positions
    positions.append(index)
    return find_positions_recursive(a, b, index + 1, positions)"""
#Ejercicio 4
"""4. Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
1 es impar.
Si un número es impar, su antecesor es par; y viceversa."""

"""def odd(n):
    if n == 1:
        return True
    elif n == 0:
        return False
    else:
        return even(n - 1)
def even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return odd(n - 1)"""


#Ejercicio 5
"""5. Escribir una función recursiva que encuentre el mayor elemento de una lista."""


"""def higher_in_list(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_rest = higher_in_list(lista[1:])
        if lista[0] > max_rest:
         return lista[0]
        else:
          return max_rest"""

#Ejercicio 6
"""6. Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])"""


"""def replicate(lista,num): 
    if num == 1:
        return lista
    else:
        new_list = []
        for i in lista:
            new_list.extend([i] * num)
        return replicate(new_list, num - 1)"""
