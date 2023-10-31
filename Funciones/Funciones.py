import math
import random
#Ejercicio Funciones
def most(a,b):
    if a > b:
        return a
    else:
        return b

def least(a,b):
    if a < b:
        return a
    else:
        return b    

#Suma de digitos EjFunciones
def sum_digits(number, sum = 0):
    while number != 0:
        digit = number % 10
        number //= 10
        sum += digit 
    print(f"Suma: {sum}")
    
#Ahorcado   
def guess_word(random_word, temporal_word, new_word, tries):
    while tries != 0 and new_word != random_word:
        letter = input("Ingrese una letra para adivinar la palabra: ")
        if random_word.find(letter) != -1:
            print("Adivinaste una letra correctamente")
            i = 0
            for r in random_word:
                if r == letter:
                    temporal_word = temporal_word[:i] + letter + temporal_word[i+1:]
                    new_word = temporal_word
                i += 1    
            print(new_word)
        else: 
            tries -= 1
            if tries == 0:
                print("No te quedan mas intentos")
            else:
                print(f"Letra incorrecta, te quedan {tries} intentos")
                print(new_word) 
                
    if new_word == random_word:
        print("Adivinaste la palabra correctamente") 
    else:
        print(f"Perdiste, la palabra es {random_word}")            
  
    
#TP5   
def login(user, password, attempt):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        attempt += 1
        return False
      
def vector_magnitude(a,b,c):
    magnitude = math.sqrt(a**2 + b**2 + c**2)
    print(f"La magnitud de un vector que tiene componentes {a,b,c} es {abs(magnitude)}")
  
def prime_number(number):
    prime_numb = True
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    
    if count > 2:
        prime_numb = False
    
    return prime_numb

def factorial(number):
    factorial = 1    
    for n in range(1, number+1):
        factorial *= n
        
    print(f"El factorial de {number} es {factorial}")
         
       
#Bingo
def fill_cardboard(cardboard, numbers):
    i = 1
    for c in cardboard:
        count = 0
        print(f"Llenar carton n°{i}")
        i += 1
        while count != 5:
            number = int(input(f"Ingrese el {count+1} numero en un rango de 1 a 75: "))
            if number < 1 or number > 75:
                print("Numero ingresado fuera de rango.")
            else:
                if number in numbers:
                    print("El numero ya se encuentra en la lista. ")
                    continue
                else:
                    count += 1 
                    numbers.append(number)
                    c.append(number) 
    
    return cardboard                
                                  
def show_cardboard(cardboard):
    print("Carton: ")   
    for c in cardboard:    
        print(c)   
        
def horizontal_line(cardboard):
    for c in cardboard:
        if c.count("x") == 5:
            return True
    return False


"""def horizontal_line(cardboard, bingo):
    for c in cardboard:
        if c.count("x") == 5:
            bingo = True
        else:
            bingo = False
    return bingo  """      

def vertical_line():
    print("")    
    
def diagonal_line():
    print("")   
    
    
#TP6 y TP7
def show_list(list_numbers):  
    for i in list_numbers:
        print(i, end = " ") 
    print(" ")      

def bubble_sort(numbers_list):
    exchange = True

    while exchange == True:
        exchange = False
        for i in range(1, len(numbers_list)):
            if numbers_list[i-1] > numbers_list[i]:
                aux = numbers_list[i-1]
                numbers_list[i-1] = numbers_list[i]
                numbers_list[i] = aux
                exchange = True
                
def selection_sort(numbers_list):
    for i in range(0, len(numbers_list)): 
        smallest = i 
        for j in range(i+1, len(numbers_list)):
            if numbers_list[j] < numbers_list[smallest]:
                smallest = j
        aux = numbers_list[i]
        numbers_list[i] = numbers_list[smallest]
        numbers_list[smallest] = aux
            
def insert_sort(numbers_list):
    for i in range(1, len(numbers_list)): 
        value = numbers_list[i]
        j = i - 1
        while j >= 0 and numbers_list[j] > value:
            numbers_list[j+1] = numbers_list[j]
            j -= 1
        numbers_list[j+1] = value
        
def merge_sort(numbers_list):
    if len(numbers_list) > 1:
        middle = len(numbers_list) // 2
        left_half = numbers_list[:middle]  
        right_half = numbers_list[middle:]  
        
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                numbers_list[k] = left_half[i]
                i += 1
            else:
                numbers_list[k] = right_half[j]
                j += 1
            k += 1
       
        while i < len(left_half):
            numbers_list[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            numbers_list[k] = right_half[j]
            j += 1
            k += 1     
            
def linear_search(numbers_list):
    find_number = int(input("Ingrese el numero que quera buscar: "))
    seEncontro = False

    for i in range(0, len(numbers_list)):
        if numbers_list[i] == find_number:
            seEncontro = True
        
    print(f"El numero {find_number} se encuentra en la lista. {seEncontro}")
    
def binary_search(numbers_list):
    find_number = int(input("Ingrese el numero que quera buscar: "))

    left = 0 
    right = len(numbers_list) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2
    
        if numbers_list[middle] == find_number:
            result = middle
            break
        elif numbers_list[middle] < find_number:
            left = middle + 1
        else:
            right = middle - 1
    
    if result != -1:
        print(f"El elemento {find_number} se encuentra en la posición {result}.")
    else:
        print(f"El elemento {find_number} no se encuentra en la lista.")
    
    
#TP8-Recirsion
def digits(number):
    if number < 10:
        return 1
    else:
        return 1 + digits(number//10)
    
def power_of_b(n,b):
    if n == 1:
        return True
    elif n % b != 0:
        return False
    return power_of_b(n / b,b)

def choose_route(minutes, total_minutes):
    route = random.randint(1,3)
    if route == 1:
        minutes = 3
        total_minutes += minutes
        print("Elijió el camino de 3 minutos y volvió a la jaula")
        
    elif route == 2:
        minutes = 5
        total_minutes += minutes
        print("Elijió el camino de 5 minutos y volvió a la jaula")
        
    elif route == 3:
        minutes = 7
        total_minutes += minutes
        print("Elijió el camino de 7 minutos y logró salir de la jaula")
        print(f"Tardo en salir de la jaula {total_minutes} minutos")
        return total_minutes
    
    return choose_route(minutes, total_minutes) 

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))
                          