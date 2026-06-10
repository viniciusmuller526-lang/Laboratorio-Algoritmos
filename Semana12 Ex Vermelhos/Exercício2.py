#Crux Sacra Sit Mihi Lux

QUANTIA_VALORES = 8

def menu():

    valores = []

    for i in range(QUANTIA_VALORES):

        valor = float(input("Insira o valor em kg da produção: "))
        valores.append(valor)

    return valores

def media (valores):
    
    soma_kg = 0

    for valor in valores:
        
        soma_kg += valor

    media = soma_kg / QUANTIA_VALORES

    print("A média foi de", media,"kg por produção")

    for i in range(len(valores)):

        if valores[i] > media:

            print("A produção", i+1, "ficou acima da média")

def main():

    valores = menu()
    media(valores)

main()
