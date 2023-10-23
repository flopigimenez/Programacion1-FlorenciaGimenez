"""8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor 
desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones."""
#Ejercicio 8
base_salary = float(input("Ingrese el salario base: "))

sale1 = float(input("Ingrese el monto de la primera venta: "))
sale2 = float(input("Ingrese el monto de la segunda venta: "))
sale3 = float(input("Ingrese el monto de la tercera venta: "))

commission = (sale1 + sale2 + sale3) * 0.10
total_money = base_salary + commission

print(f"El monto total de comisión es: {commission}")
print(f"El salario total que recibirá en el mes es: {total_money}")