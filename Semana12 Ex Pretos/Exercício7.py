#Crux Sacra Sit Mihi Lux

QUANT_VALORES = 6

def solicitar_valores():

    valores = []
    rendimento = 0

    for i in range(QUANT_VALORES):

        valor = int(input("Insira a quantia de kg de azeitonas por lote:"))
        valores.append(valor)

    rendimento = int(input("Insira a porcentagem de rendimento da extração: ")) / 100

    return valores, rendimento

def multiplicacao(valores, rendimento):

    print("Estimativa de produção em litros:")

    for i in range(QUANT_VALORES):

        litros = valores[i] * rendimento
        print("Lote", i+1,":", litros, "litros de azeite")

def main():

    valores, rendimento = solicitar_valores()
    multiplicacao(valores, rendimento)

main()
