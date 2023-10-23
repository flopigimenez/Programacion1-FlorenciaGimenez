"""17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje 
diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de 
esos, imprimir otro mensaje."""
#Ejercicio 17
day = input("Ingrese un dia de la semana: ")

if day.lower() == "lunes":
    print("Es lunes. Arranca la semana")
elif day.lower() == "viernes":
    print("Es viernes. Ya casi es fin de semana")
elif day.lower() == "sabado" or day.lower() == "domingo":
    print("Ya es fin de semana")
elif day.lower() == "martes" or day.lower() == "miercoles" or day.lower() == "jueves":
    print("No es un día relevante de la semana.")
