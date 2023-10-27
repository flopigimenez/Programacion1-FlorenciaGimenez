"""1. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente 
forma: (nombre, dni, destino). Por ejemplo:
*('Manuel Juarez', 12345678, 'San Juan'), ('Silvana Paredes', 62258472, 'Mendoza')+
Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
*('Buenos Aires', 'Argentina'), ('Lisboa', 'Portugal'), ('Mendoza', 'Argentina')+
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa."""
#Ejercicio 1
passengers_data = [(),()]
place_data = [(),()]

while True:
    print("----------------Menú----------------")
    print("""1. Agregar pasajeros a la lista de viajeros.
    2. Agregar ciudades a la lista de ciudades.
    3. Dado el DNI de un pasajero, ver a qué ciudad viaja.
    4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
    5. Dado el DNI de un pasajero, ver a qué país viaja.
    6. Dado un país, mostrar cuántos pasajeros viajan a ese país.
    7. Salir del programa.""")
    option = int(input("Ingrese el numero de la opcion que desea realizar: "))
    salir = "no"
    if option == 1:
        while salir.lower() != "si":
            for p in passengers_data:
                count = 0
                while count != 3:
                    print("Ingrese el nombre del pasajero: ")

     