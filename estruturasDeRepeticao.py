

# exemplo de iteraveis:
# string "Oi"
# lista [1,2,3]
# range (1,10)

"""
nome = "renata"
enumerate(nome) = ((0,'R'),(1'E'))
"""




if __name__ == "__main__":
    nome = "Renata"
    lista = [1,2,3,4,5]
    numeros = range(1,10) # vai de 1 a 9
    #iterando sobre uma string
    for letra in nome:
        print(letra, end='')
    #iterando sobre lista
    for num in lista:
        print(num)
    #iterando sobre range
    for num in numeros:
        print(num)
    
    for _, letra in enumerate(nome):
        print(letra)
    
    for valor in enumerate(nome):
        print(valor)
        print(valor[0])


    #OBS: Quando nao precisamos de um valor, descartamos com um _
    #nome *  3 = renatarenatarenata

    # mostra os nomes sendo multiplicados
    for num in range(1,10):
        print(nome*num)

    # faz uma arvorezinha
    for x in range(3):
        for num in range (1,5):
            print('\U0001F604'*num)


    pass






    
    