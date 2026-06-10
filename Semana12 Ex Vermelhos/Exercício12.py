#Crux Sacra Sit Mihi LUx

QUANTIA_VALORES = 5

def menu():

    kg_colhido = []
    preco_por_kg = []

    for i in range(QUANTIA_VALORES):

        valor = int(input("Insira a produção em kg da árvore: "))
        kg_colhido.append(valor)
        valor = int(input("Insira o valor por kg da árvore: "))
        preco_por_kg.append(valor)

    return kg_colhido, preco_por_kg

def multipliclação(kg_colhido, preco_por_kg):

    multiplicação_valores = []

    for i in range(QUANTIA_VALORES):

        multiplicação = kg_colhido[i] * preco_por_kg[i]
        multiplicação_valores.append(multiplicação)

    return multiplicação_valores

def resultado(multiplicação_valores):
    
    print("Valor obtido por árvore:")
    
    for i in range(QUANTIA_VALORES):

        print("Árvore", i+1, ":", multiplicação_valores[i],"reais")


def main():

    kg_colhido, preco_por_kg = menu()
    multiplicação_valores = multipliclação(kg_colhido, preco_por_kg)
    resultado(multiplicação_valores)

main()
