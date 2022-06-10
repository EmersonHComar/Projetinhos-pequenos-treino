def verifica():
    while True:
        try:
            num = int(input("Digite um número natural(0= sair): "))
            if num >= 0:
                return num
            else:
                print("Digite apenas um número natural")
        except:
            print("Digite apenas um número natural")

def nmrsDecimais(numero):
    casas = 0
    zeros = 1
    
    while int(numero) >= 1:
        casas += 1
        numero /= 10
        zeros *= 10
    return casas, zeros

def escreve(numero, casas, zeros):
    
    lista = [[1, "unidade(s)"],[2, "dezena(s)"],[3, "centena(s)"],
        [4, "unidade(s) de milhar"],[5, "dezena(s) de milhar"],
        [6, "centena(s) de milhar"],[7, "unidade(s) de milhão"],
        [8, "dezena(s) de milhão"],[9, "centena(s) de milhão"]]
    
    print("\n")
    while casas > 0:
        zeros /= 10
        cont = 0
        for indice, palavra in lista:
            if indice == casas:
                while int(numero) >= zeros:
                    numero -= zeros
                    cont += 1
                if cont != 0:
                    print("%d --> %s" %(cont, palavra))
        casas -= 1
while True:
    numero = verifica()
    if numero == 0:
        break
    casas, zeros = nmrsDecimais(numero)
    escreve(numero, casas, zeros)
    print("\n")