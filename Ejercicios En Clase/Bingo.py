import sys
sys.path.append('C:/Users/BIENVENIDO/Desktop/Programación/Programación 1/Repositorio Programacion1 - Florencia Gimenez/Programacion1-FlorenciaGimenez/Funciones')
import Funciones
import random
cardboard = [[],[],[],[],[]]
numbers = []

cardboard = Funciones.fill_cardboard(cardboard, numbers)  

Funciones.show_cardboard(cardboard)               

print("Inicia el juego") 
bingo = False

while bingo == False: 
    for count in range(5):
        ball_number = random.randint(1,75)
        if  ball_number in numbers:
            print(f"El numero {ball_number}, si esta en el carton")
            index_number = numbers.index(ball_number)
            numbers[index_number] = 'x'
            cardboard = [x if x != ball_number else 'x' for x in cardboard]
            
            #Funciones.vertical_line()
            #Funciones.diagonal_line()
        else:
            print(f"El numero {ball_number}, no esta en el carton") 
        
        #ball_number not in numbers      
    bingo = Funciones.horizontal_line(cardboard)
    
    if bingo:
        print("Bingo")              