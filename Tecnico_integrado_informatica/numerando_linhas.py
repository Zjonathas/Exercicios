"""Faça um programa que abre um arquivo de texto qualquer (crie um pra fazer o teste) e
acrescente no início de cada linha uma numeração. O programa deve exibir o conteúdo
com as linhas adicionadas como no exemplo abaixo:
001: texto qualquer
002: qualquer texto
003: outro texto aleatório qualquer"""
try:
    abrir = open('qualquer.txt', 'x')
    abrir.close()
except FileExistsError:
    with open('qualquer.txt', 'r+', encoding='utf_8') as p:
        contador = 0
        for linha in p:
            contador += 1
            print(contador, linha, end='')
