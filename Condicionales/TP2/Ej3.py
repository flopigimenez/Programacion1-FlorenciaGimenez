"""3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
A continuación. Imprimir 'coincidencia' si ambos nombres comienzan con la misma letra. Si no es así, imprimir 
'no hay coincidencia'."""
#Ejercicio 3
name1 = input("Ingrese un nombre: ")
name2 = input("Ingrese otro nombre: ")

if name1[0].lower() == name2[0].lower():
    print("Coincidencia")
else:
    print("No hay coincidencia")