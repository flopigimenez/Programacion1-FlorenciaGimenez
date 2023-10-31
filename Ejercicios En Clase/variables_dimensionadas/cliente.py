def custumers(list_of_costumers):
    single_address = set()

    for buy in list_of_costumers:
        client, _, _, address = buy
        single_address.add(address)

    biling_address = list(single_address)

    return biling_address
new_list = []
while(True):
    print("----Menu----")
    print("1-Carga de clientes")
    print("2-Salir")
    choice = int(input("Ingrese la operacion que desea realizar: "))
    if choice == 1:
        while(True):
            eleccion = int(input("Si desea salir ingrese O, si desea continuar 1: "))
            if eleccion == 0:
                break
            else:
                client = input("Ingrese el nombre del cliente: ")
                day_of_month = int(input("Imgrese el dia del mes: "))
                amount = float(input("Ingrese el monto de la compra: "))
                client_adress = input("Ingrese la direccion del cliente: ")
                client_tuple = (client, day_of_month, amount, client_adress)
                new_list.append(client_tuple)
        domicilios = custumers(new_list)
        print(domicilios)

    else:
        break




