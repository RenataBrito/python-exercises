"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parêntese()
2 - As tuplas são imutaveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova tupla 
Não existe um append por exemplo


tupla1 = (1,2,3,4,5,6)
tupla2 = 1,2,3,4,5,6 # mesmo sem parenteses na criacao ela vira uma tupla mas no print aparece os parenteses
print(type(tupla1))
print(tupla1)
print(type(tupla2))
print(tupla2)

tupla3 = (4) # isso não é uma tupla, é um inteiro
tupla4 = (4,) # isso é uma tupla

# tuplas sao definidas pela !!VIRGULA!! e nao pelo uso dos parenteses

# tupla dinamica a partir do range
tupla = tuple(range(11))
print(tupla)

#desempacotamento
# gera erro se colocarmos um numero diferente de variaveis pra receber da tupla
tupla = ("Renata", 'Pedro','Rebecca')
pessoa, irmao, irma = tupla
print(pessoa)
print(irmao)
print(irma)


# metodos para adição e remoção de elemetos nas tuplas nao existem dado o fato das tuplas serem imutaveis
# sum max min len vale tbm, mas tem que ser valores numericos


# Concatenação de tuplas

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)

# Verificar se determinado elemento esta contido na tupla
tupla = 1,2,3

print(4 in tupla)

# iterando sobre uma tupla

tupla = 1,2,3
for i in tupla:
    print(i)

for indice, valor in enumerate(tupla):
    print(indice,valor)


# Contando elementos dentro de uma tupla

tupla = 'a','b','c','d','a','b'
print(tupla.count('a'))

nome = tuple('Renata')
print(nome.count('a'))

# Dicas na utilização de tuplas
# quando n vamos mudar os dados da colecao
# ex: meses

#acesso de elementos

tupla = 1,2,3,4,5
print(tupla[0])

#iterar com while
i = 0
while i < len(tupla):
    print(tupla[i])
    i+=1


# verificar se tem na lista, caso nao exista gera um erro
tupla = 1,2,3,4,5
print(tupla.index(2))

# Slicing

tupla = 1,2,3,4,5
print(tupla[2:4])


"""

# PQ USA TUPLA?
# Tuplas são mais rapidas do q listas.
# Tuplas deixa seu codigo mais seguro


