#Crux Sacra Sit Mihi Lux

QUANTIA_VALORES = 5

def menu():

    valores = []

    for i in range(QUANTIA_VALORES):

        valor = float(input("Insira o valor em kg da produção: "))
        valores.append(valor)

    return valores

def reverter(valores):

    print("Ordem Contrária:")

    for i in range(4,-1,-1):

        print(valores[i],"kg")
        
def main():

    valores = menu()
    reverter(valores)

main()
