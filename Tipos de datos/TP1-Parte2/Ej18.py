"""18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, 
sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar."""
#Ejercicio 18
dinner_cost = int(input("Ingrese cuanto costó la cena: "))
final_cost = dinner_cost + (dinner_cost * 0.062) + (dinner_cost * 0.10)
print(f"El monto final a pagar es {final_cost}")