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

#Bucle que verifica sin la letra está en la palabra hasta que no tenga mas intentos o adivine la palabra
while tries != 0 and new_word != random_word:
    letter = input("Ingrese una letra para adivinar la palabra: ")
    if random_word.find(letter) != -1:
        print("Adivinaste una letra correctamente")
        i = 0
        for r in random_word:
            if r == letter:
                temporal_word = temporal_word[:i] + letter + temporal_word[i+1:]
                new_word = temporal_word
            i += 1    
        print(new_word)
    else: 
        tries -= 1
        if tries == 0:
            print("No te quedan mas intentos")
        else:
            print(f"Letra incorrecta, te quedan {tries} intentos")
            print(new_word)

if new_word == random_word:
    print("Adivinaste la palabra correctamente") 
else:
    print(f"Perdiste, la palabra es {random_word}")                                    