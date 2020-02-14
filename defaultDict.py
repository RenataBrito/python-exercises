"""
Modulo Collections - defaultdict, evitar o erro

Ao criar o dic ulilizando um valor default, podendo utilizar 
um lamba pra isso. Este valor sera utilizado sempre que nao houver
um valor definido. Caso tentamos aessar uma chave que nao existe,
essa chave sera criada e o valor default vai nela.

lamba = funcoes sem novo que pode ou nao receber parametros de entrar, e podem ou nao retornar valores


"""
from collections import defaultdict


dicionario = defaultdict(lambda : 0)
dicionario['curso'] = 'Eng comp'
dicionario['outro']
print(dicionario)