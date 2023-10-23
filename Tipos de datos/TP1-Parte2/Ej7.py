"""7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas 
y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos."""
#Ejercicio 7
minutes = int(input("Ingrese los minutos: "))
hours = int(minutes / 60)
min = minutes % 60

print(f"{minutes} minutos son {hours} horas y {min} minutos.")
