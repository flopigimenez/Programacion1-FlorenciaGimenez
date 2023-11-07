import Funciones_parcial
dna_list = []

#Llenar el array 
for i in range(6):
    dna = Funciones_parcial.enter_dna(i) 
    dna_list.append(dna)
    
print("------------------------")    
print("Secuencia de adn")    
for d in dna_list:
    print(d)
    
mutant = Funciones_parcial.is_mutant(dna_list)

print(f"Es mutante {mutant}")


"""dna_list = ['ACTGTA','AGATGT','TCTAAC','GTGCAA','AGGGGA','ATGTCC'] 
Es mutante True
- Tiene 2 lineas diagonales y 1 horizontal"""

"""dna_list = ['AGGCTG','ACGTGC','CCGCAG','CCCGTG','ACACGC','TCTAGA'] 
Es mutante False
- Solo tiene una linea vertical"""