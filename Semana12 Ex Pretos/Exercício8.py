#Crux Sacra Sit Mihi Lux

QUANT_VALORES = 10

def checagem():

    valores = []

    while len(valores) != QUANT_VALORES:

        valor = int(input("Insira um código de RFID: "))

        if valor > 1000:

            valores.append(valor)

        else:

            print("Código inválido, insira novamente")

    return valores

def main():

    valores = checagem()
    print(valores)

main()
