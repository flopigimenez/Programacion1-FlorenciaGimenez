"""9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A 
está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
el grupo que le corresponde."""
#Ejercicio 9
name = input("Ingrese su nombre: ")
gender = input("Ingrese su sexo(femenino/masculino): ")

letters_name1 = "abcdefghijklm"
letters_name2 = "nñopqrstuvwxyz"

count1 = letters_name1.count(name[0].lower())
count2 = letters_name2.count(name[0].lower())

if count1 == 1 and gender.lower() == "femenino" or count2 and gender.lower() == "masculino":
    print("Corresponde al grupo A")

elif count2 == 1 and gender.lower() == "femenino" or count1 and gender.lower() == "masculino":
    print("Corresponde al grupo B")
