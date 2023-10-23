"""18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora. La jornada de trabajo 
mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas 
laborales comunes."""
#Ejercicio 18
hours = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salary_per_hour = int(input("Ingrese el salario por hora: "))
minimum_hous = 48
salary = hours * salary_per_hour

if hours > minimum_hous:
    extra_percentage = salary * 0.10
    salary += extra_percentage
    print(f"Trabajó horas extras, su salario es de ${salary}")
else:
    print(f"Su salario es de ${salary}")