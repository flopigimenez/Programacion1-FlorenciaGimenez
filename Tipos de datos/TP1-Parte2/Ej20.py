"""20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA."""
#Ejercicio 20
day = int(input("Ingrese el dia de su nacimiento: "))
month = int(input("Ingrese el mes de su nacimiento: "))
year = int(input("Ingrese el año de su nacimiento: "))

DDMMAA = str(day) + "/" + str(month) + "/" + str(year)
print(f"Fecha de nacimiento {DDMMAA}")