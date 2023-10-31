passengers = []
cities = []

while True:
    print("------------------MENÚ------------------")
    print("1. Agregar pasajeros a la lista de viajeros")
    print("2. Agregar ciudades a la lista de ciudades")
    print("3. Dado el dni de un pasajero, ver a qué país viaja")
    print("4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
    print("5. Dado el DNI de un pasajero, ver a qué país viaja")
    print("6. Dado un país, mostrar cuántos pasajeros viajan a ese país")
    print("7. Salir")

    choice = int(input("Ingresa el número de la operación que deseas realizar: "))

    if choice == 1:
        while True:
            eleccion = int(input("Si deseas continuar ingresa 1, si deseas salir 0: "))
            if eleccion == 0:
                break
            else:
                name = input("Ingresa el nombre del pasajero: ")
                dni = int(input("Ingresa el DNI: "))
                destination = input("Ingresa la ciudad de destino: ")
                person = (name, dni, destination)
                passengers.append(person)

    elif choice == 2:
        eleccion = int(input("Si deseas continuar ingresa 1, si deseas salir 0: "))
        if eleccion == 0:
            break
        else:
            city = input("Ingresa la ciudad: ")
            country = input("Ingresa el país: ")
            origin = (city, country)
            cities.append(origin)


    elif choice == 3:
        dni_choose = int(input("Ingresa el dni: "))
        for person in passengers:
            if person[1] == dni_choose:
                for city in cities:
                    print(person[0] + " viaja a " + person[2] + " que pertenece a " + city[1])
            else:
                print("El dni no pertenece a ningun pasajero")

    elif choice == 4:
        country_choose = input("Ingresa el país que deseas averiguar: ")
        count = 0
        for person in passengers:
            if person[2] == country_choose:
                count += 1
        print("Hay " + str(count) + " pasajeros viajando a " + country_choose)

    elif choice == 5:
        dni_search = int(input("Ingresa el DNI del pasajero: "))
        for person in passengers:
            if person[1] == dni_search:
                for city in cities:
                    if city[0] == person[2]:
                        print(person[0] + " viaja a " + city[1])
                break
        else:
            print("No se encontró ningún pasajero con ese DNI.")

    elif choice == 6:
        pais_search = input("Ingresa el nombre del país: ")
        count = 0
        for person in passengers:
            for city in cities:
                if person[2] == city[0] and city[1] == pais_search:
                    count += 1
        print("Hay " + str(count) + " pasajeros viajando a " + pais_search)

    elif choice == 7:
        break

    else:
        print("El número ingresado es incorrecto")
