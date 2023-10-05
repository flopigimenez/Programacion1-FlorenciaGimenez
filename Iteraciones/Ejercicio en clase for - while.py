#Ejercicio 1 - for
abecedario = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

mensajes = []
for i in range(5):
    mensajes.append(input(f'Ingrese el mensaje num {i}: '))


corrimiento = int(input(f'Indique el corrimiento: '))

mensajes_encrip = []

for mensaje in mensajes:
    palabra_temporal = ""
    for letra in mensaje:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + corrimiento) % 27
            letra_temporal = abecedario[nuevo_indice]
            palabra_temporal += letra_temporal
        else:
            palabra_temporal += letra
    mensajes_encrip.append(palabra_temporal)  


for mensaje in mensajes_encrip:
    print(mensaje)  
    
#Ejercicio 2 - while
peers = 0
odd = 0
num = 1

while num > 0:
    num = int(input("Ingrese un numero mayor a 0: "))
    if num % 2 == 0:
        peers += 1
    else:
        odd += 1
        
print(f"La cantidad de numeros pares ingresados: {peers}") 
print(f"La cantidad de numeros impares ingresados: {odd}")