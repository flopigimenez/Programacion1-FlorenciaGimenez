"""1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola 
que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años."""
#Ejercicio 1
computer_years = int(input("Ingrese los años de su computadora: "))

if computer_years <= 2:
    print("El coputador es nuevo.")
else:
    print("El computador es viejo.")