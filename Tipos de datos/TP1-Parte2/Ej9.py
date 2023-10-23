"""9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
cuanto deberá pagar finalmente por su compra."""
#Ejercicio 9
buy_price = float(input("Ingrese el precio de la compra: "))

percentage = buy_price * 0.15
total_price = buy_price - percentage

print(f"Con el descuento el cliente deberá pagar por su compra ${total_price}")