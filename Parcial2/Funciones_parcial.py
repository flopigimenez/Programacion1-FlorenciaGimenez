def enter_dna(i):
    while True:
        dna = input(f"Ingrese la {i+1}° secuancia de adn. Debe contener 6 letras, y estas solo pueden ser A,T,C,G: ").upper()
        #verifico si contiene 6 letras
        if len(dna) != 6:
            print("Secuencia incorrecta, debe tener 6 letras.")
        else:
            #Verifico si se ingresan letras diferentes a las permitidas
            verify_dna = verify_letter(dna)
            if verify_dna == False:
                print("Secuencia incorrecta, solo puede contener las letras A,T,C,G.")
            else:
                print("Secuencia Correcta")
                break
    return dna        
     
def verify_letter(dna):
    for d in dna:
        if d == "A" or d == "T" or d == "C" or d == "G":
            verify_letter = True
        else:
            verify_letter = False
            break
    return verify_letter   

def is_mutant(dna_list): 
    letter = "ATCG"
    h = 0
    v = 0
    d = 0
    
    #Verifica si hay una linea de 4 letras iguales
    for l in letter:   
        if horizontal_line(dna_list, l) == True:
            print(f"linea horizontal de {l}")
            h += 1
        if vertical_line(dna_list, l) == True:
            print(f"linea vertical de {l}")
            v += 1
        if diagonal_line(dna_list, l) == True:
            print(f"linea diagonal de {l}")
            d += 1
    
    if (h >= 1 and v >= 1) or (h >= 1 and d >= 1) or (v >= 1 and d >= 1):
        return True
    if h > 1 or v > 1 or d > 1: 
        return True
    return False
    
#verificación horizontal 
def horizontal_line(dna_list, l):
    for d in dna_list:
        horizontal_line = ""
        for i in d:
            if i == l:
                horizontal_line += l
                if len(horizontal_line) >= 4:
                    return True
            else:
                horizontal_line = ""
    
    return False

#verificación vertical
def vertical_line(dna_list, l):
    for i in range(6):
        vertical_line = ""  
        for d in dna_list:
            if d[i] == l:
                vertical_line += l
                if len(vertical_line) >= 4:
                    return True
            else:
                vertical_line = "" 
    return False

#verificación diagonal
def diagonal_line(dna_list, l):
    for d in range(len(dna_list)-3): 
        for j in range(len(dna_list[d])-3):
            diagonal_line = ""
            for x in range(4):
                if dna_list[d + x][j + x] == l:
                    diagonal_line += l
                    if len(diagonal_line) >= 4:
                        return True    
                else:
                    break       
    
    for d in range(len(dna_list)-3): 
        for j in range(len(dna_list[d])-3):
            diagonal_line = ""
            for x in range(4):
                if dna_list[d + 3 - x][j + x] == l:
                    diagonal_line += l
                    if len(diagonal_line) >= 4:
                        return True    
                else:
                    break 
    return False         