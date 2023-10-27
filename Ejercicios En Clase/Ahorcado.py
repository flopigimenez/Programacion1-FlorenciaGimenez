import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
import random
print("Ahorcado")

words_list = ["hola", "ejemplo", "palo", "vaca", "zapatilla", "sapo", "computadora", "perro", "gato", "montaña", 
"television", "edificio", "oceano", "astronauta", "guitarra", "bosque", "pelicula", "bicicleta", "playa", 
"jirafa", "camion", "chocolate", "reloj", "rio", "elefante", "biblioteca"]

#elije una palabra random
random_word = random.choice(words_list)

temporal_word = ""
new_word = ""
tries = len(random_word)

#muestra con guiones bajos la cantidad de letras de la palabra
print("Palabra: ", end="")
for i in range(0,len(random_word)):
    temporal_word += "_"
    new_word += "_"
print(temporal_word)

#Llama a la funcion que verifica si la letra está en la palabra hasta que no tenga mas intentos o adivine la palabra
Funciones.guess_word(random_word, temporal_word, new_word, tries)

                                    