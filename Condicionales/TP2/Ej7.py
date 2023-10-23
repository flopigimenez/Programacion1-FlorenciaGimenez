"""7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres."""
#Ejercicio 7
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))
number3 = int(input("Ingrese el tercer numero: "))

if number1 < number2 and number1 < number3:
    print(f"El numero {number1} es el menor")
elif number2 < number1 and number2 < number3:
    print(f"El numero {number2} es el menor")
elif number3 < number1 and number3 < number2:
    print(f"El numero {number3} es el menor")