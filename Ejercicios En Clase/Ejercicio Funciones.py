import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
"""1. El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, 
y=1 pero en su lugar imprime 5. ¿Qué hay que corregir"""
x = int(input("Ingrese un numero entero: "))
y = int(input("Ingrese otro numero entero: "))

print(Funciones.most(x-3, Funciones.least(x+2, y-5)))