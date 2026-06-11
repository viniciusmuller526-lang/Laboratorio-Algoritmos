#Crux Sacra Sit Mihi Lux

NUM_VALORES = 10

def pedir_valores():

    valores = []

    for i in range(NUM_VALORES):

        valor = input("Insira um lote: ")
        valores.append(valor)

    return valores

def reverter(valores):

    print("Ordem inversa:")

    for i in range(NUM_VALORES-1, -1, -1):

        print(valores[i])

def main():

    valores = pedir_valores()
    reverter(valores)

main()
