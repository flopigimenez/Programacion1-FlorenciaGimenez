"""13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
que el usuario escriba “salir” que terminará."""
#Ejercicio 13
entry = input("Ingrese una palabra o numero: ")

#entra a un bucle en el que se imprime lo que ingresa el usuario hasta que se deje de cumplir la condicion
while entry.lower() != "salir":
    print(entry)
    entry = input("Ingrese una palabra o numero, si quiere salir ingrese salir: ")

