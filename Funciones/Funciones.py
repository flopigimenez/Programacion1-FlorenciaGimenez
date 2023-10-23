def sum_digits(number, sum = 0):
    while number != 0:
        digit = number % 10
        number //= 10
        sum += digit 
    print(f"Suma: {sum}")
    
