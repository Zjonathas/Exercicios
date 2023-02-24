"""Crie um programa que recebe uma lista de inteiros e um valor que deve ser buscado. O programa deve retornar o
índice onde o valor foi encontrado, ou -1, caso não encontre o valor."""


lista_de_inteiros = input('Digite uma lista de inteiros: ').split(' ')
valor_a_ser_buscado = input('Digite o valor que você deseja procurar: ')

if valor_a_ser_buscado in lista_de_inteiros:
    for i, v in enumerate(lista_de_inteiros):
        if valor_a_ser_buscado == v:
            print(i)
else:
    print('-1')
