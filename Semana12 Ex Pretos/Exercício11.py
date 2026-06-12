#Crux Sacra Sit Mihi Lux

import random

QUANT_IDS = 10

def gerar_ids():

    lotes = []

    for i in range(QUANT_IDS):

        lote = random.randint(1,50)
        lotes.append(lote)

    return lotes

def impar_par(lotes):

    pares = []
    impares = []

    for lote in lotes:

        if lote % 2 == 0:

            pares.append(lote)

        else:

            impares.append(lote)

    print("Quantia de pares: ", len(pares))
    
    for par in pares:

        print("-", par)
    
    print("Quantia de impares: ", len(impares))
    
    for impar in impares:

        print("-", impar)

def main():

    lotes = gerar_ids()
    impar_par(lotes)

main()
