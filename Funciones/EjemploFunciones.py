import Funciones

"""Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos."""
sum_numbers = 0

while True: 
    number = int(input("Ingrese un numero: "))
    if number == 0:
        break
    else:
        Funciones.sum_digits(number)
        sum_numbers += number
      
"""Al finalizar mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos.""" 
print("---------------------------------------------------")  
print(f"Suma numeros: {sum_numbers}")
Funciones.sum_digits(sum_numbers)