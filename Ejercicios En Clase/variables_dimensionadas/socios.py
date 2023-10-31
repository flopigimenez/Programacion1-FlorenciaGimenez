socios = {
   1:  {"nombre": "Amanda Núñez", "ingreso": "17/03/2009", "cuota_al_dia": "s"},
   2: {"nombre": "Bárbara Molina", "ingreso": "17/03/2009", "cuota_al_dia": "s"},
   3: {"nombre": "Lautaro Campos", "ingreso": "17/03/2009", "cuota_al_dia": "s"}
}
while True:
    print("------------------MENÚ------------------")
    print("1-Carga de socios")
    print("2-Catidad de socios")
    print("3-Corregir fecha de ingreso")
    print("4-Dar baja a socio")
    print("5-Pago de cuotas")
    print("6-Imprimir listado de socios")
    print("7-Salir")
    choice = int(input("Ingresa el número de la operación que deseas realizar: "))

    if choice == 1:
        while True:
            eleccion = int(input("Si deseas continuar ingresa 1, si deseas salir 0: "))
            if eleccion == 0:
                break
            else:
                num = int(input("Ingrese el numero de socio: "))
                name = input("Imgrese el nombre del socio: ")
                date = input("Ingrese la fecha de ingreso en el formato (ddmmaaaa): ")
                pay = input("Posse la cuota al dia? s/n")
                socios[num] = {"nombre": name, "ingreso": date, "cuota_al_dia": pay}
    if choice == 2:
        print("La cantidad de socios es: " + str(len(socios)))
    if choice == 3:
        for num_of_member, datos in socios.items():
            if datos["ingreso"] == "13/03/2018":
                datos["ingreso"] = "14/03/2018"
    if choice == 4:
        name_delete = input("Ingrese el miembro que desea dar de baja: ")
        for num_of_member, datos in socios.items():
            if datos["nombre"] == name_delete:
                del socios[num_of_member]
                print(" El socio " + name_delete + "ha sido dado de baja.")
                break
    if choice == 5:
        num_of_member = int(input("Ingrese el numero de socio al que desea informar su pago : "))
        if num_of_member in socios:
            socios[num_of_member]["cuota_al_dia"] = "s"
    if choice == 6:
        print("Listado de Socios:")
        for num_of_member, datos in socios.items():
            cuota_estado = "al día" if datos["cuota_al_dia"] else "adeudada"
            print("Socio n°: " + str(num_of_member) + datos['nombre'] +" ingresó: " + datos['ingreso'] +" cuota " + cuota_estado)
    if choice == 7:
        break





