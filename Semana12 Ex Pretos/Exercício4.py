#Crux Sacra Sit Mihi Lux

QUANT_VALORES = 5

def solicitar_valores():

    valores = []

    for i in range(QUANT_VALORES):

        valor = int(input("Insira a quantia em kg de azeitonas colhidas: "))
        valores.append(valor)

    return valores

def soma(valores):

    soma_total = 0

    for valor in valores:

        soma_total += valor

    print("A soma das colheitas é: ", soma_total, "kg")

    return soma_total

def media(soma_total):

    media = soma_total/QUANT_VALORES
    print("A quantia média de kg por colheita é de: ", media, "kg")

def main():

    valores = solicitar_valores()
    soma_total = soma(valores)
    media(soma_total)

main()
