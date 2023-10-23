"""15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""
#Ejercicio 15
number = int(input("Ingrese un número entero mayor que cero: "))

#entra a un bucle en el que evalua la condicion t si es verdadera muetra los divisore del numero pedido al ususario
print(f"Los divisores de {number} son:", end= " ")
for i in range(1,number+1):
    if number % i == 0:
        print(i, end= " ")
        
