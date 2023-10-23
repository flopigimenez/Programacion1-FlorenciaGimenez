"""12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.""" 
#Ejercicio 12
phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
letter_found = 0

#entra a un bucle que sirve como contador para cuando se cumple la condición
for i in phrase:   
    if i == letter:
        letter_found += 1
    
print(f"La letra {letter} aparece {letter_found} veces en la frase")

