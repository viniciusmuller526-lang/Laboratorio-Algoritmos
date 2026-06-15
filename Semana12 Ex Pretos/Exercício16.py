#Crux Sacra Sit Mihi Lux

import random

QUANT_CONFRONTOS = 5

def array_forca_colheita():

    forca_colheita = []

    for i in range(QUANT_CONFRONTOS):

        forca = float(input("Insira a força do lote contra a praga: "))
        forca_colheita.append(forca)

    return forca_colheita

def array_forca_praga():

    forca_praga = []

    for i in range(QUANT_CONFRONTOS):
    
        forca = round(random.uniform(1, 100), 2)
        forca_praga.append(forca)

    return forca_praga

def confronto(forca_colheita, forca_praga):

    lotes_protegidos = []
    lotes_perdidos = []

    for i in range(QUANT_CONFRONTOS):

        if forca_colheita[i] > forca_praga[i]:
            
            print("Força Colheita: ", forca_colheita[i])
            print("Força Praga: ", forca_praga[i])
            print("Colheita salva!")
            lotes_protegidos.append(i)

        else:
            
            print("Força Colheita: ", forca_colheita[i])
            print("Força Praga: ", forca_praga[i])
            print("Colheita perdida!")
            lotes_perdidos.append(i)

    print("Lotes protegidos: ")

    for lotes in lotes_protegidos: 
        
        print(lotes+1)
    
    print("Lotes perdidos: ")

    for lotes in lotes_perdidos:

        print(lotes+1)

def main():

    forca_col = array_forca_colheita()
    forca_pra = array_forca_praga()
    confronto(forca_col, forca_pra)

main()
