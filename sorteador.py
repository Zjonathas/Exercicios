from random import randint

# Separação dos nomes dos integrantes e nomes dos tópicos do tema
nomes = []
topicos = []

# Aqui é armazenado os resultados que já saíram para não se repetir
nomes_sort = []
topicos_sort = []

while len(nomes_sort) < len(nomes) and len(topicos_sort) < len(topicos):
    num_nome = randint(0, len(nomes)-1)
    num_topicos = randint(0, len(topicos)-1)
    if num_nome in nomes_sort or num_topicos in topicos_sort:
        continue
    nomes_sort.append(num_nome)
    topicos_sort.append(num_topicos)
    print(f'{nomes[num_nome]} ficou com {topicos[num_topicos]}')
