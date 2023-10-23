"""5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)
c)	edad = int(input(“Edad: “))
print(tu edad es, edad)
d)	edad = int(input(“Edad: “))
print(“Veamos si tu edad es 18…”, edad=18)"""
#Ejercicio 5
#a)
nombre = input("Ingresed su nombre: ")
A = input(f"{nombre}, ¿Cuál es tu canción favorita?: ")
print(A)

#b)
precio = int(input("Precio: "))
total = precio + (precio * 0.1)
print(total)

#c)
edad = int(input("Edad: "))
print(f"Tu edad es, {edad}")

#d)
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad==18)
