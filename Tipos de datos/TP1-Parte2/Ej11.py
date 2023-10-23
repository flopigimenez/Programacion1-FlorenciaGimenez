"""11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su 
diferencia, de modo que el resultado sea siempre positivo)."""
#Ejercicio 11
number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

diference = abs(number1 - number2)

print(f"La diferencia ente {number1} y {number2} es {diference}")