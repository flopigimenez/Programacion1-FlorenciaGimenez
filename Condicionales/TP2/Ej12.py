"""12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado 
desde ese año o cuántos años faltan para llegar a ese año."""
#Ejercicio 12
actual_age = int(input("Ingrese el año actual: "))
age = int(input("Ingrese cualquier año: "))

if actual_age > age:
    print(f"Desde {age} hasta {actual_age} han pasado {actual_age - age} años")
else:
    print(f"Para llegar a {age} faltan {age - actual_age} años")