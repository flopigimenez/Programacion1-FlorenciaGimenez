"""2- Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo."""
#Ejercicio 2
computer_years = int(input("Ingrese los años de su computadora: "))

if computer_years < 0:
    print("Error. Debe ingresar un numero positivo")
elif computer_years <= 2:
    print("El coputador es nuevo.")
else:
    print("El computador es viejo.")