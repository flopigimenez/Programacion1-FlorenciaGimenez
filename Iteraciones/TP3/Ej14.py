"""14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y 
cuáles impares desde el primero hasta el segundo."""
#Ejercicio 14
number1 = (int(input("Ingrese el primer numero: ")))
number2 = (int(input("Ingrese el segundo numero: ")))

#entra a un bucle en el que si la condicion es verdadera muestra los numeros pares
print(f"Numeros pares entre {number1} y {number2}: ", end= " ")
for i in range(number1,number2 +1):
    if i % 2 == 0:
        print(i, end=" ")

print(" ")
#entra a un bucle en el que si la condicion es verdadera muestra los numeros impares
print(f"Numeros impares entre {number1} y {number2}: ", end= " ")
for i in range(number1,number2+1):
    if i % 2 != 0:
        print(i, end=" ")

print(" ")
    
