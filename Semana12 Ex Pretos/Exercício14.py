#Crux Sacra Sit Mihi Lux

QUANT_ETIQUETAS = 15

def inserir_etiqueta():

    codigos = []

    while len(codigos) != QUANT_ETIQUETAS:

        etiqueta = int(input("insira uma etiqueta: "))

        repetidos = False

        for codigo in codigos:

            if codigo == etiqueta:

                repetidos = True
                break

        if repetidos == False:

            codigos.append(etiqueta)

        elif repetidos == True:

            print("Este código já foi adicionado, tente outro")

    return codigos

def main():

    codigos = inserir_etiqueta()
    print(codigos)

main()
