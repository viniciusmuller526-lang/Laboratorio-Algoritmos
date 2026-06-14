#Crux Sacra Sit Mihi Lux

QUANT_LOTES = 5

def solicitar_lotes():

    lotes = []

    for i in range(QUANT_LOTES):

        lote = int(input("Insira o código do lote: "))
        lotes.append(lote)

    return lotes

def checar_repeticao(lotes):
    
    repetidos = False

    for i in range(len(lotes)):

        checador = lotes[0]
        lotes.pop(0)

        for lote in lotes:

            if lote == checador:

                repetidos = True
                break

        lotes.append(checador)

    if repetidos == False:

        print("Distintos")

    elif repetidos == True:

        print("Há duplicatas")

def main():

    lotes = solicitar_lotes()
    checar_repeticao(lotes)

main()
