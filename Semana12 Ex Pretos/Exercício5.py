#Crux Sacra Sit Mihi Lux

QUANT_VALORES = 5

def solicitar_valores():

    valores = []

    for i in range(QUANT_VALORES):

        print("Insira a quantidade de kg colhidos da árvore", i+1)
        valor = int(input("Insira a quantia:"))
        valores.append(valor)

    return valores

def encontrar_maior_menor (valores):

    maior = 0
    menor = 0
    posmaior = 0
    posmenor = 0

    if not valores:

        print("Lista vazia, tente novamente")
        return
    
    else:

        for i in range(len(valores)):

            if i == 0:

                maior = valores[i]
                menor = valores[i]
                posmaior = i
                posmenor = i

            else:

                if valores[i] > maior:

                    maior = valores[i]
                    posmaior = i

                elif valores[i] < menor:

                    menor = valores[i] and i
                    posmenor = i

    print("Maior quantia de kg colhidos: ", maior, "kg, árvore", posmaior+1)
    print("Menor quantia de kg colhidos: ", menor, "kg, árvore", posmenor+1)

def main():

    valores = solicitar_valores()
    encontrar_maior_menor(valores)

main()
