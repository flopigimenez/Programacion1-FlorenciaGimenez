import math
#Suma de digitos EjFunciones
def sum_digits(number, sum = 0):
    while number != 0:
        digit = number % 10
        number //= 10
        sum += digit 
    print(f"Suma: {sum}")
    
#Numero primo TP5-Ej13    
def vector_magnitude(a,b,c):
    magnitude = math.sqrt(a**2 + b**2 + c**2)
    print(f"La magnitud de un vector que tiene componentes {a,b,c} es {abs(magnitude)}")
 
#Numero primo TP5-Ej14  
def prime_number(number):
    prime_numb = True
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    
    if count > 2:
        prime_numb = False
    
    return prime_numb

#Factorial TP5-Ej15
def factorial(number):
    factorial = 1    
    for n in range(1, number+1):
        factorial *= n
        
    print(f"El factorial de {number} es {factorial}")
         