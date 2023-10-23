"""19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe 
un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento."""
#Ejercicio 19
pencil = int(input("Ingrese la cantidad de lapices que quiere comprar: "))
price = pencil * 60

if pencil >= 1000:
    discount = price * 0.07
    price -= discount
else:
    price = price
    
print(f"Si compras {pencil} lapices el precio final es de ${price}")
