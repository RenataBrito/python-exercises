"""
Em alguma linguagens de programação, os dicionario Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

OBS: Sobre dicionarios
    - Chave e valor são separados por dois ponto 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;



# Formas de representar dicionarios

paises = {'br': 'Brasil', 'eua':'Estados Unidos','py':'Paraguai'} #chave : valor
print(paises)

paises = dict(br='Brasil',eua='Estatos Unidos',py='Paraguai')
print(paises)

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

paises = {'br': 'Brasil', 'eua':'Estados Unidos','py':'Paraguai'} #chave : valor
print(paises['br']) # imprime os valores atraves das chaves, se pesquisar uma chave que nao existe vai da erro

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru')) # quando nao tem o elemento ele da "None" => Tipo sem tipo, considerado com falso 

russia = paises.get('br')
if russia:
    print('Encontrei o país.')
else:
    print('N encontrei o país.')


pais = paises.get('lu','nao encontrado')
print(f'Encontrei o país {pais}')
print(paises)

# Verificar se tem o objeto a partir da chave e nao o valor

print('br' in paises)
print('Brasil' in paises)

if 'ru' in paises:
    russia = paises['ru']
    print(russia)

# Tuplas é interessante para usar como chave de dicionario pois elas nao mudam
localidades = {
    (35.6895,39.6917): 'Escritorio em Tókio',
    (40.7128,79.6917): 'Escritorio em Sp',
    (37.6895,122.6917): 'Escritorio em Rj',
}
print(localidades)

# Adicionar elementos em um dicionário

receita = {'jan':100,'fev':120,'mar':300}
print(receita)
receita['abr'] = 350
print(receita)
novo_dado = {'mai':500}
receita.update(novo_dado)
print(receita)

# Atualizando
receita['mai']=550
print(receita)
receita.update({'mai':600})
print(receita)

# A forma de adicionar novos elementos ou atualizar dados em um dic é a mesma forma
# Não podemos ter chaves repetidas

# Remover dados de um dic, com pop e del

print(receita)
receita.pop('mar')

# Devemos informar a chave para tirar, caso nao encontre vai da erro
print(receita)

del receita['fev'] # o valor removido nao é retornado
print(receita)

# criando um carrinho de compras
carrinho = []
produto1 = {'nome':'Play 4', 'quantidade':1,'preco':2300}
produto2 = {'nome':'God of ward', 'quantidade':1,'preco':230}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Métodos de dic
d =dict(a=1,b=2,c=3)
print(d)
d.clear()
print(d)

# deep copy
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

#shallow copy

novo = d
print(d)
novo ['d'] = 4
print(d)
print(novo)

"""

paises = {'br': 'Brasil', 'eua':'Estados Unidos','py':'Paraguai','ru':'russia'} #chave : valor
receita = {'jan':100,'fev':120,'mar':300}

# o metodo fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

veja = {}.fromkeys('teste','valor')
print(veja)

veja = {}.fromkeys(range(1,11),'valor')
print(veja)



