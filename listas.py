"""
Listas

listas em python funciona como vetores/matrizes, pode ser Dinamicos e podemos colocar qualquer tipo de dado

- Em C o vetor tem só um tipo.

- Dinâmico em python não possui tamanho fixo

!!! Em python representamos a lista por colchetes: []   !!!!!

# Valor contido em uma lista
num = 18

if num in lista4:
    print(f'Encontrei o {num}')
else:
    print(f'Não encontrei o numero {num}')


if 'e' in lista5:
    print(f'Encontrei a letra e')
else:
    print(f'Não encontrei a letra e')

# Ordenar a lista
lista1.sort() # ordenar numeros
lista5.sort() # ordenar letras
print(lista1)
print(lista5)

# contar na lista a ocorrencia de algum valor
print(lista1.count(1))
print(lista5.count('a'))

# adicionar elementos em lista usar a funcao append
print(lista1)
lista1.append(42)
print(lista1)

# O append so adiciona um elemento por vez no final da fila
lista1.append([8,3,1]) #adicionando uma lista
print(lista1)

# o extend coloca cada elemento de uma lista como valor adicional a lista
lista1.extend([36,99,85])
lista1.remove([8,3,1])
lista1.sort() #nao da pra ordenar a lista com uma lista dentro
print(lista1)

#inserir um elemento informando sua posicao
lista1.insert(2,'novo valor') #  substitui oq tive na posicao, oq estava so desloca
print(lista1)

# juntar duas listas e mudando ela
lista1.reverse()
lista6 = lista1 + lista2
print(lista6)

#contar quantos elementos existem dentro da lista
print(len(lista1))

#remover o ultimo elemento da lista, pop remove o ultimo elemento e o retorna
print(lista5)
lista5.pop()
print(lista5)

#remover um elemento pelo indice, se nao houver item no indice vai da index error
lista5.pop(2)
print(lista5)

# zerar a lista
lista5.clear()
print(lista5)

#repetir elementos em uma lista
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)


#converter string pra lista
curso = "Engenharia de computação"
print(curso)
curso = curso.split() # coloca um espaço entre as palavras dentro da lista
print(curso)

curso = 'Teste,De,Msg'
curso = curso.split(',') #o seprador entre as palavras agora é ,
print(curso)


# pega a lista 7 coloca espaço em cada elemento e transforma em uma string
lista7 = ["esse", "dia",'esta']
print(lista7)
curso = ' '.join(lista7) # adiciona o espaco mas pode ser qualquer coisa
print(curso)

#iterando sobre a lista
for elemento in lista1:
    print(elemento)

carrinho = []
produto = ""
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

carrinho.sort()
print(carrinho) 

# acessar de forma indexada, da erro caso queira acessar uma posicao vazia 

print(lista1[0])
print(lista1[1])
print(lista1[-4]) #começa la do fim

#Gerar indice em um for
cores =["amarelo", 'verde','azul']
for indice, cor in enumerate(cores):
    print(indice,cor)

#encontrar o indice de um elemento na lista
numeros = [5,6,7,8,9,10]
print(numeros.index(5)) #caso nao tenha o elemento na lista vai da erro, e retorna o indice do primeiro elemento encontrado

#escolher qual indice comecar a buscar
print(numeros.index(8,0)) #busca a partir do indice 0
print(numeros.index(8,0,4)) #busca a partir do  0 ate o 3 

#Trabalhando com slice de lista
lista =[1,2,3,4]
print(lista[1:])
print(lista[-3:])
print(lista[:2])

#invertendo os valores
nomes = ['renata','mae']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

#ou nomes.reverse()

#Soma, Valor Maximo, Valor minimo, Tamanho

lista = [1,2,3,4]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

#lista -> tupla
lista = [1,2,3,4]
print(lista)
tupla = tuple(lista)
print(tupla)

#desempacotamento

lista = [1,2,3,4]
num1,num2,num3,num4 = lista
print(num1)

#shallow copy e deep copy
#modifica uma lista nao afeta a outra = deep copy
lista = [1,2,3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)

#shallow copy
lista = [1,2,3]
print(lista)
nova = lista
print(nova)
nova.append(4)
print(lista)
print(nova)

"""

type([])
lista1 = [1,55,3,4,5,6]
lista2 = ['a','b','c']
lista3 = []
lista4 = list(range(11)) #gera numeros de 0 a 10
lista5 = list('Renata brito')



