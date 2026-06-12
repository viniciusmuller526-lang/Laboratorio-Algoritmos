#Crux Sacra Sit Mihi Lux

import random

def gerar_filtrar_ids():

    lotes = []

    for i in range(10):

        lote = random.randint(1,100)
        lotes.append(lote)
    
    for lote in lotes:

        if lote % 2 == 0:

            print("-", lote)

def main():

    gerar_filtrar_ids()

main()
