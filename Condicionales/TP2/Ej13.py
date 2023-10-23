"""13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
Haciendo que el programa avise cuando se escriben valores negativos o nulos."""
#Ejercicio 13
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

if number1 <= 0 or number2 <= 0:
    print("Error. Alguno de los numero ingresados es negativo o nulo")
elif number1 > number2:
    if number1 % number2 == 0:
        print(f"{number1} es multiplo de {number2}")
    else:
        print(f"{number1} no es multiplo de {number2}")
else:
    if number2 % number1 == 0:
        print(f"{number2} es multiplo de {number1}")
    else:
        print(f"{number2} no es multiplo de {number1}")