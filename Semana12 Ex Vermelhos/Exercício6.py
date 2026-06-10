#Crux Sacra Sit Mihi Lux

QUANTIA_VALORES = 5

def menu():

    fazenda_a = []
    fazenda_b = []

    for i in range(QUANTIA_VALORES):

        valor = int(input("Insira o valor em kg da produção da fazenda A: "))
        fazenda_a.append(valor)

    for i in range(QUANTIA_VALORES):

        valor = int(input("Insira o valor em kg da produção da fazenda B: "))
        fazenda_b.append(valor)

    return fazenda_a, fazenda_b

def soma(fazenda_a, fazenda_b):

    soma_fazendas = []

    for i in range(QUANTIA_VALORES):

        soma = fazenda_a[i] + fazenda_b[i]
        soma_fazendas.append(soma)

    return soma_fazendas

def resultado(fazenda_a, fazenda_b, soma_fazendas):

    print("Fazenda A:")
    
    for i in range(QUANTIA_VALORES):

        print("Lote", i+1, ":", fazenda_a[i],"kg")    
        
    print("Fazenda B:")
    
    for i in range(QUANTIA_VALORES):

        print("Lote", i+1, ":", fazenda_b[i],"kg")    
        
    print("Soma dos lotes:")
    
    for i in range(QUANTIA_VALORES):

        print("Lote", i+1, ":", soma_fazendas[i],"kg")


def main():

    fazenda_a, fazenda_b = menu()
    soma_fazendas = soma(fazenda_a, fazenda_b)
    resultado(fazenda_a, fazenda_b, soma_fazendas)

main()
