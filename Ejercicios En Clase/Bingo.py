import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
import random
salir = "no"
while salir.lower() != "si":
    cardboard = [[],[],[],[],[]]
    numbers = []

    cardboard = Funciones.fill_cardboard(cardboard, numbers)  

    Funciones.show_cardboard(cardboard)               

    print("Inicia el juego") 
    bingo = False

    while bingo == False: 
        print("")
        for count in range(5):
            ball_number = random.randint(1,75)
            if  ball_number in numbers:
                print(f"El numero {ball_number}, si esta en el carton")
            
                index_number = numbers.index(ball_number)
                numbers[index_number] = 'x'
            
                for i in range(5):
                    for j in range(5):
                        if cardboard[i][j] == ball_number:
                            cardboard[i][j] = 'x'
                            
                h_bingo = Funciones.horizontal_line(cardboard)
                v_bingo = Funciones.vertical_line(cardboard)
                d_bingo = Funciones.diagonal_line(cardboard)
    
                if h_bingo == True or v_bingo == True or d_bingo == True:
                    print("Bingo")
                    bingo = True
                    break
            
            else:
                print(f"El numero {ball_number}, no esta en el carton")  
     
    print("------------------------------------------")        
    salir = input("Quiere salir del juego?(si/no): ") 
    print("")       