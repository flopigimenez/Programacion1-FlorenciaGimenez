"""Realizar un programa que cumpla con las siguientes condiciones:
Pedir al usuario su nombre. Cada vez que el programa interactúe con él debe llamarlo por su nombre.
Generar un menú de opciones, que serán:
Juego de números.
Juego de palabras.
Si el usuario elige la primera opción, se debe pedir el ingreso de números enteros (condición de salida: 
cuando ingrese 0). Al finalizar mostrar por pantalla:
El mayor número par.
El promedio de los números impares.
Si el usuario elige la segunda opción, se debe pedir el ingreso de una frase y mostrar por pantalla 
la cantidad de cada vocal que contiene dicha frase.
No olvides realizar las debidas validaciones!"""

name = input("Ingrese su nombre: ")
print(f"Bienvenido/a {name}, elija una de las opciones: ")
print("a.Juego de numeros")
print("b.Juego de palabras")
options = input()

#Si el usuario elije la opcion "a" entra al bucle if sino evalua nuevamente la condicion y si es una b
# ingresa al elif
if options.lower() == "a":
    number = 1
    max_even_number = 0
    odd_numbers = 0
    sum = 0
    
    #evalua la condicion, si es verdadera va a continuar ejecuatandose
    while number != 0:
        number = int(input("Ingrese un numero entero: "))
       
        #evalua si los numeros  son pares o impares y se ejecuta el codigo correspondiente
        if number % 2 == 0:
            if number > max_even_number:
                max_even_number = number
        else:
            sum += number
            odd_numbers += 1    #contador
               
    average = sum / odd_numbers
    print(f"El mayor numero par ingresado es {max_even_number}") 
    print(f"El promedio de los numeros impares ingresados es {average}")
    
elif options.lower() == "b":
    vowel_list = ["a","e","i","o","u"]
    sentence = input("Ingrese una frase: ").lower()
    
    #entra al bucle for donde recorre la frase
    for s in sentence:
        #utilizo la funcion count() para saber cuantas veces se encuntra cada vocal
        count_a = sentence.count(vowel_list[0])   
        count_e = sentence.count(vowel_list[1])
        count_i = sentence.count(vowel_list[2])
        count_o = sentence.count(vowel_list[3])
        count_u = sentence.count(vowel_list[4])
    
    print(f"a: {count_a}")
    print(f"e: {count_e}") 
    print(f"i: {count_i}") 
    print(f"o: {count_o}") 
    print(f"u: {count_u}")     
                
    