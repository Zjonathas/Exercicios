"""Construa um algoritimo de busca binária"""


def busca_binaria(lista, posicao_inicial, posicao_final, elemento_a_ser_encontrado):
    if posicao_final <= posicao_final:  # Condição de existência
        meio_da_lista = (posicao_inicial + posicao_final) // 2  # Índice do meio da lista
        if elemento_a_ser_encontrado > lista[meio_da_lista]:
            return busca_binaria(lista, meio_da_lista + 1, posicao_final, elemento_a_ser_encontrado)
        elif elemento_a_ser_encontrado < lista[meio_da_lista]:
            return busca_binaria(lista, posicao_inicial, meio_da_lista - 1, elemento_a_ser_encontrado)
        else:
            return meio_da_lista  # Elemento encontrado
    else:
        return -1


array = list(range(0, 100))
print(array)
elemento = 9
posicao = busca_binaria(array, 0, len(array) - 1, elemento)

if posicao >= 0:
    print(f'O elemento "{elemento}" foi encontrado na posição {posicao}')
else:
    print(f'O elemento "{elemento}" não foi encontrado')
