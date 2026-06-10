#Crux Sacra Sit Mihi Lux

def menu():

    print("----------- Menu de gerenciamento de lotes -----------")
    print("")
    print("1 - Inserir lote")
    print("2 - Listar lotes")
    print("3 - Retirar um lote")
    print("4 - Limpar todos os lotes")
    print("5 - Contar quantos lotes têm produção maior que X")
    print("6 - Verificar se um código está presente")
    print("7 - Encontrar maior e menor código no array")
    print("8 - Sair")
    print("")
    print("------------------------------------------------------")
    print("")

    try:
        
        opcao = int(input("Escolha uma opcão: "))

    except ValueError:

        print("Opção inválida, tente novamente")

    else:

        if opcao < 1 or opcao > 8:

            print("Opção inválida, tente novamente")

        else:

            return opcao
        
def inserir_lote(lotes):

    lote = int(input("Insira um lote: "))

    if lote % 2 == 0:

        lotes.append(lote)
        
        return lotes

    else:

        print("Lote inválido, insira um lote par")

        return lotes

def listar_lotes(lotes):

    for i in range(len(lotes)):

        print("Item", i+1, ":", lotes[i])

def retirar_lote(lotes):

    excluir_lote = int(input("Insira um lote que deseja remover: "))

    if excluir_lote in lotes:

        lotes.remove(excluir_lote)
        return lotes
    
    else:

        print("Este lote não está na lista")
        return lotes

def limpar_lotes(lotes):

    lotes = []

    return lotes

def contar_lotes_maior_x(lotes):

    quantia = 0

    valor_checagem = int(input("Insira o valor para checar lotes maiores que este valor: "))

    for i in range(len(lotes)):

        if lotes[i] > valor_checagem:

            quantia += 1

    print("Há", quantia, "lotes maiores que", valor_checagem)

def verificar_lote(lotes):

    lote_checagem = int(input("Insira o lote que deseja checar: "))

    if lote_checagem in lotes:

        print("O lote", lote_checagem, "está na lista")

    else:

        print("Lote", lote_checagem, "não está na lista")

def encontrar_maior_menor (lotes):

    maior = 0
    menor = 0

    for i in range(len(lotes)):

        if i == 0:

            maior = lotes[i]
            menor = lotes[i]

        else:

            if lotes[i] > maior:

                maior = lotes[i]

            elif lotes[i] < menor:

                menor = lotes[i]

    print("Maior lote: ", maior)
    print("Menos lote: ", menor)

def main():

    lotes = []
    opc = 0
    
    while opc != 8:

        opc = menu()

        if opc == 1:

            lotes = inserir_lote(lotes)

        elif opc == 2:

            listar_lotes(lotes)

        elif opc == 3:

            lotes = retirar_lote(lotes)

        elif opc == 4:

            lotes = limpar_lotes(lotes)
        
        elif opc == 5:

            contar_lotes_maior_x(lotes)
        
        elif opc == 6:

            verificar_lote(lotes)

        elif opc == 7:

            encontrar_maior_menor(lotes)


main()
