"""6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser 
divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
#Ejercicio 6
leap_year = int(input("Ingrese un año: "))

if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print(f"El año {leap_year} es un año bisiesto")
else:
    print(f"El año {leap_year} no es un año bisiesto")