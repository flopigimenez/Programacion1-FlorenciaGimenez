import random
import getpass

print("PIEDRA PAPEL O TIJERA")
nombre =input("Ingrese su nombre: ")
choice = input( nombre + ", ingrese cualquier tecla para comenzar el juego: ")
point_machine=0
point_game=0
        #Se inicializan variables y empieza el juego si el usuario ingresa un numero correctamente
print("A JUGAR!!")
opcion= ["PIEDRA", "PAPEL", "TIJERA"]
winner = True
opc2 = int(input("Ingrese 1 si desea jugar con la maquina y 2 si desean ser 2 jugadores: "))

if opc2 == 1:
    while(winner):
        play = input("Ingresa tu eleccion: Piedra, papel o tijera: ")  
        play = play.upper() 
            #Entramos a un bucle while donde el usuario ingresara su eleccion y la convertimos en mayuscula
        if play == "PIEDRA" or "PAPEL" or "TIJERA":
            play_bot = random.randint(0, 2)
            #Ingresamos a un if donde filtramos segun el valor ingresado por el usuario y el valor ingresado por la maquina a travez de un random.randint
            if opcion[play_bot] == play:
                print("¡EMPATE!")
            elif opcion[play_bot]== "PIEDRA" and play == "PAPEL":
                point_game += 1
                print("La maquina eligio: "+ opcion[play_bot])
            elif opcion[play_bot]== "PAPEL" and play == "PIEDRA":
                point_machine +=1
                print("La maquina eligio: "+ opcion[play_bot])
            elif opcion[play_bot] == "PIEDRA" and play == "TIJERA":
                point_machine +=1
                print("La maquina eligio: "+ opcion[play_bot])
            elif opcion[play_bot] == "TIJERA" and play =="PIEDRA":
                point_game +=1
                print("La maquina eligio: "+ opcion[play_bot])
            elif opcion[play_bot] == "PAPEL" and play == "TIJERA":
                point_game +=1
                print("La maquina eligio: "+ opcion[play_bot])
            elif opcion[play_bot] == "TIJERA" and play == "PAPEL":
                point_machine +=1
                print("La maquina eligio: "+ opcion[play_bot]) 

            print()
            print("maquina: " + str(point_machine) + " - " + " jugador: " + str(point_game))
            #Un if que validara si el jugador o la maquina llegan a tener 3 puntos par adarle la victoria
            if point_game == 3:
                print("¡GANASTE!")
                break
            elif point_machine == 3:
                print("Gana la maquina :(")
                break
        else:
            print("Ingreso una palabra incorrecta")
elif opc2 == 2:
    point_player1= 0
    point_player2= 0
    while(winner):
        #Los usuarios ingresan piedra papel o tijera
        player1 = getpass.getpass('Jugador 1, ingrese piedra, papel o tijera: ')
        player1 = player1.upper()
    
        player2 = getpass.getpass('Jugador 2, ingrese piedra, papel o tijera: ')
        player2 = player2.upper()

        #Sus respuestas entran en varios if y elif enlazados que funcionan como contadores para conseguir el ganador 
        if player1 and player2 in opcion:
            if player1 == 'PIEDRA' and player2 == 'TIJERA':
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                point_player1 += 1
            elif player1 == 'PAPEL' and player2 == 'PIEDRA':
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                point_player1 += 1
            elif player1 == 'TIJERA' and player2 == 'PAPEL':
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                point_player1 += 1
            elif player1 == 'TIJERA' and player2 == 'PIEDRA':
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                point_player2 += 1
            elif player1 == 'PAPEL' and player2 == 'TIJERA':
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                point_player2 += 1
            elif player1 == 'PIEDRA' and player2 == 'PAPEL':
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                point_player2 += 1
            else:
                print(f'Jugador 1: {player1}, Jugador 2: {player2}')
                print('empate')
            
            print()
            print("Jugador 1: " + str(point_player1) + " - " + " Jugador 2: " + str(point_player2))

            
            if point_player1 == 3:
                print("¡EL JUGADOR 1 GANO!")
                break
            elif point_player2 == 3:
                print("¡EL JUGADOR 2 GANO!")
                break
        else:
            print('Una de las dos opciones fue ingresada incorrectamente...')
            continue