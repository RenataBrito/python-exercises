"""
Mapas -> Conhecidos em python como Dicionarios
Dicionarios em python são representados por chave {}

#iterar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}')


print(receita.keys())


for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(receita[chave])

#acesso aos valores
for valor in receita.values():
    print(valor)
"""

receita = {'jan':200,'fev':250,'mar':300}
print(receita)

#desempacotamento de dic

print(receita.items())

for chave, valor in receita.items():
    print(f'chaves={chave} e valor={valor}')