#Crux Sacra Sit Mihi Lux

def codigos(call):

    codigos = [13, 14, 22, 27]

    if call in codigos:

        print("Encontrado")

    else:

        print("Não encontrado")

def chamar_codico():

    call = int(input("Insira um código: "))

    return call

def main():

    call = chamar_codico()
    codigos(call)

main()
