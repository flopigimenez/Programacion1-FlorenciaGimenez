"""14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba 
la solución.Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o 
que todos los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a"""
#Ejercicio 14
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))

if a == 0:
    if b == 0:
        print("La ecuación {a}x + {b} = 0 tiene infinitas soluciones.")
    else:
        print("La ecuación {a}x + {b} = 0 no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación {a}x + {b} = 0 es x = {x}")