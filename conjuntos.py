"""
Conjunto = Sets, não possuem valores duplicados, nao possuem valores ordenados
elementos nao sao acessador via indice.

Conjuntos nao sao indexados.

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos mas 
nao nos importamos com a ordenação deles, quando nao nos preocupamos com chaves, valores e itens duplicados.

Os conjuntos são referenciados com chaves {}


DIFERENÇA ENTRE CONJUNTOS E MAPAS
    - Dicionario tem chave/valor;
    - Um conjunto tem apenas valor;

# Def Conj

# Forma 1

s =set({1,2,3,4,5,5,6,7,2,3}) #valor repetidos sao ignorados
print(s)
print(type(s))

# Forma 2
s = {1,2,3,4,5,5}
print(s)
print(type(s))

if 3 in s:
    print(f'tem o 3')
else:
    print('nao tem o 3')

# Importante lembrar alem de nao ter valores duplicados, nao temos ordem
s = {99,2,34,23,12,1,44,5,2,34} # nao pode valor replicado
lista = [99,2,34,23,12,1,44,5,2,34] # pode ter duplicados
tupla = (99,2,34,23,12,1,44,5,2,34) # pode ter duplicados
dicionario={}.fromkeys(lista,'dict') # nao aceita chave duplicada
print(f'lista {lista} com {len(lista)} elementos')
print(f'tupla {tupla} com {len(tupla)} elementos')
print(f'dicionario {dicionario} com {len(dicionario)} elementos')
print(f'conjunto {s} com {len(s)} elementos')

 # USO INTERESSANTE DE SETS

 # formulario de visitantes de museu, pode vir uma excurção de sp,
 # com isso vai ter cidade repetidas, mas se vc querer descobrir cidades distintas usa sets. BOAAA

# adicionando elemento
s = {1,2,3}
s.add(4)
print(s)

# remover elemento
# forma 1
s.remove(3) # não é indice é valor, se nao encontrar o valor da erro, nenhum valor é retornado
print(s)

# forma 2
s.discard(2) # n gera erro se nao encontrar o valor
print(s)

# copiando um conjunto para outro
s = {1,2,3}
d = {5,6,7,8}
print(s)

# deep copy
novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

#shallow copy

novo = s
novo.add(4)
print(novo)
print(s)

# remover todos os elementos
s = {1,2,3}
s.clear()
print(s)

"""
# operacoes de conjunto

# uniao

estudade_p = {'renata','pedro','tania','rebecca'}
estudade_j = {'renata','lucio','tania','rebecca','pedro'}
unicos14 = estudade_p.union(estudade_j)
print(unicos14)

# outra forma
unicos2 = estudade_p | estudade_j
print(unicos2)

# interseção
ambos1 = estudade_p.intersection(estudade_j)
print(ambos1)

ambos2 = estudade_p & estudade_j
print(ambos2)

# diferença

sop = estudade_p.difference(estudade_j)
soj = estudade_j.difference(estudade_p)
print(sop)
print(soj)

