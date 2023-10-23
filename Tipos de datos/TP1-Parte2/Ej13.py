"""13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
Ejemplo, si se introduce 23 que muestre 32."""
#Ejercicio 13
number = int(input("Ingrese un numero de dos cifras: "))

if number > 9 and number < 100:    
    number1 = number % 10
    number1 *= 10

    number2 = number // 10
    
    if number1 == 0:
        number1 = str(number1)
        number2 = str(number2)
        print(f"El número {number} invertido es {number1 + number2}")
    else:
        print(f"El número {number} invertido es {number1 + number2}")
else:
    print("El número no es de dos cifras")