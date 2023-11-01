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
#Ej 1
def dni_verification(document):
    if (len(document) == 7) or (len(document) == 8):
        valid = True
    else:
        valid = False
    return valid

#Ej 2
def last_word_lenght(w_list):
    last_word = w_list[-1]
    l_w_length = len(last_word)

    return l_w_length

#Ej 3
def name_verification(m_name):
    valid_name = True
    if (len(m_name) < 2) or (len(m_name) > 3):
        valid_name = False
    
    return valid_name

def member_id_generator(m_name, dni):
    first_name = str(m_name[0]).replace(',', '').strip().capitalize()
    last_name_length = str(len(m_name[-1]))
    first_numbers_dni = str(dni[0:3])
    member_id = str(first_name + last_name_length + first_numbers_dni)
    return member_id

#Ej 4
def is_multiple(a, b):
    if a % b == 0:
        return print('El primer número ingresado es múltiplo del segundo.')
    else:
        return print('El primer número no es múltiplo del segundo')
    
#Ej 5    
def avg_temperature(max_temp, min_temp):
    return (max_temp + min_temp) / 2

#Ej 6
def return_wh_spaces(a_string):
    new_string = ""
    for character in a_string:
        if character.isalpha():
            new_string += character + " "
        else:
            new_string += character
    return new_string

#Ej 7
def mayor_menor(number_list):
    el_mayor = number_list[0]
    el_menor = number_list[0]
    for i in number_list:
        if i > el_mayor:
                el_mayor = i
        if i < el_menor:
                el_menor = number_list[i]
    return "El mayor valor es: " + str(el_mayor) + ", el menor valor es: " + str(el_menor)

#Ej 8
def circunferencia(radius):
    area = math.pi*(radius ** 2)
    perimeter = 2 * math.pi * radius
    return "El perimetro del radio ingresado es: " + str(perimeter) + " y el area es: " + str(area)

#Ej 9
def login(user, password, attempt):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        attempt += 1
        return False

#Ej 10
def apply_discount(shopping_cart, discounts):
    final_prize= 0
    
    for product, prize in shopping_cart.items():
        if product in discounts:
            discount = discounts[product]
            discount_prize = prize * (1 - discount / 100)
            final_prize += discount_prize
        else:
            final_prize += prize
    return final_prize
 
#Ej 11
def apply_function_to_list(func, input_list):
    result = []
    for element in input_list:
        result.append(func(element))
    return result

def square(x):
    return x ** 2
 
#Ej 12
def word_length_dict(phrase):
    words = phrase.split()
    result = {}
    
    for word in words:
        result[word] = len(word)
    return result 
 
#Ej 13
def vector_magnitude(a,b,c):
    magnitude = math.sqrt(a**2 + b**2 + c**2)
    print(f"La magnitud de un vector que tiene componentes {a,b,c} es {abs(magnitude)}")

#Ej 14
def prime_number(number):
    prime_numb = True
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    
    if count > 2:
        prime_numb = False
    
    return prime_numb

#Ej 15
def factorial(number):
    factorial = 1    
    for n in range(1, number+1):
        factorial *= n
        
    print(f"El factorial de {number} es {factorial}")
    return factorial
         
       
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
    for row in cardboard:
        line = True 
        for element in row:
            if element != 'x':
                line = False  
                break 
        if line:
            print("¡Línea horizontal!")
            return True
    return False 

def vertical_line(cardboard):
    for col in range(5):  
        line = True  
        for row in cardboard:
            if row[col] != 'x':
                line = False  
                break  
        if line:
            print("¡Línea vertical!")
            return True
    return False

def diagonal_line(cardboard):
    left_to_right = True
    right_to_left = True

    for i in range(5):
        if cardboard[i][i] != 'x':
            left_to_right = False
        if cardboard[i][4 - i] != 'x':
            right_to_left = False

    if left_to_right or right_to_left:
        print("¡Línea diagonal!")

    return left_to_right or right_to_left

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

def bubble_sort_3(dictionary, key):
    n = len(dictionary)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if dictionary[j][key] > dictionary[j + 1][key]:
                dictionary[j], dictionary[j + 1] = dictionary[j + 1], dictionary[j]
    return dictionary
                
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

def selection_sort_dic(arr, key):
    n = len(arr)

    # Crear una copia de la lista de diccionarios para no modificar la original
    sorted_arr = arr.copy()

    # Iterar a través de todos los elementos de la lista de diccionarios
    for i in range(n):
        # Encontrar el índice del elemento mínimo en la lista sin ordenar
        min_index = i
        for j in range(i + 1, n):
            if sorted_arr[j][key] < sorted_arr[min_index][key]:
                min_index = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento sin ordenar
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]

    # Devolver la lista ordenada
    return sorted_arr

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

def count_sort(array):
    # Encuentra el valor máximo en la lista
    maxim = max(array)

    # Crea un arreglo auxiliar para contar las apariciones de cada número
    count = [0] * (maxim + 1)

    # Llena el arreglo de conteo con las apariciones de cada número
    for num in array:
        count[num] += 1

    # Reconstruye la lista ordenada a partir del arreglo de conteo
    array_ord = []
    for i in range(len(count)):
        for j in range(count[i]):
            array_ord.append(i)

    return array_ord
    
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
                          