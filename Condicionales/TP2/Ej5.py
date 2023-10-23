"""5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje 'Es vocal'. 
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle 
que no se puede procesar el dato."""
#Ejercicio 5
vowel = input("Ingrese una letra: ")
vowel_list = "aeiou"

count = vowel_list.count(vowel)

if len(vowel) > 1 :
    print("No se puede procesar el dato")
elif count == 1:
    print("Es vocal")
else:
    print("No es vocal")
    