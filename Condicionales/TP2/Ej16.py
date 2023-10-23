"""16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b"""
#Ejercicio 16
print("Calculadora")
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

print("Operaciones: \n1.Suma \n2.Multiplicacion \n3.Resta \n4.Division")
opc = int(input("Segun las opciones ingrese el numero de la operacion que desea realizar: "))

if opc == 1:
    operation = "suma"
    result = number1 + number2
elif opc == 2:
    operation = "multiplicacion"
    result = number1 * number2
elif opc == 3:
    operation = "resta"
    result = number1 - number2
elif opc == 4:
    operation = "division"
    result = number1 / number2
   
print(f"La {operation} entre {number1} y {number2} es {result}")