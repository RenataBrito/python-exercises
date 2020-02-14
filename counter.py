"""
Modulo Collections - Counter (contador)

counter -> recebe um iteravel como parametro e crfia um objeto do tipo collections counter que é parecido
com o dic, contendo chave e elemento da lista passada como parametro e como valor a quantidade de ocorrencias
desse elemento

# Exemplo 1, numeros
lista = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,6,6,45,48,49,89,79]

res = Counter(lista)
print(res)

# Exemplo 2, string

print(Counter('Renata')) 

"""
from collections import Counter

# Exemplo 3, as palavras que mais se repetem 

texto = """

What is Lorem Ipsum?

Lorem Ipsum is simply dummy text of the printing and
 typesetting industry. Lorem Ipsum has been the 
 industry's standard dummy text ever since the 1500s, 
 when an unknown printer took a galley of type and
  scrambled it to make a type specimen book. It has 
  survived not only five centuries, but also the leap
   into electronic typesetting, remaining essentially 
   unchanged. It was popularised in the 1960s with the 
   release of Letraset sheets containing Lorem Ipsum passages,
    and more recently with desktop publishing software like Aldus 
    PageMaker including versions of Lorem Ipsum.


"""

palavras = texto.split()
#print(palavras)
res = Counter(palavras)
#print(res)

# encontrando as 5 palavras com mais ocorrencia
print(res.most_common(5))