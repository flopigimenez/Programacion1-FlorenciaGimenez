"""4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul. Según el 
candidato elegido (A, B o C) se debe imprimir el mensaje: 'Usted ha votado por el partido [color del candidato 
elegido]. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
indicar 'Opción errónea'."""
#Ejercicio 4
vote = input(f"Partidos: \nA : rojo \nB : verde \nC : azul \nIngrese su voto: ")

if vote == 'A':
    print(f"Usted ha votado por el partido rojo")
elif vote == 'B':
    print(f"Usted ha votado por el partido verde")
elif vote == 'C':
    print(f"Usted ha votado por el partido azul")
