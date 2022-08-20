"""Faça um programa que simule um editor de textos. O programa deve perguntar ao
usuário se ele quer criar um novo texto, exibir o texto ou gerar um relatório do texto.
Na criação do texto, o usuário deve ser livre pra digitar quantas linhas quiser. No
momento que ele quiser parar de escrever ele deve iniciar uma linha com a palavra
“sair”. A opção de exibir o texto apenas exibe seu conteúdo. A opção de gerar relatório
deve apresentar os seguintes dados do texto: o número de linhas, o número total de
caracteres e o número de espaços em branco."""


def contar_espacos(string):
    espacos = 0
    string.seek(0, 0)
    for linha in string:
        for a in linha:
            if a == ' ':
                espacos += 1
    return espacos


def contar_linhas(arquiv):
    linha = 0
    for _ in arquiv:
        linha += 1
    return linha


while True:
    print('-' * 50)
    escolha = input('Escolha uma das opções:\n'
                    '1 - Criar um novo texto\n'
                    '2 - Exibir o texto\n'
                    '3 - gerar um relatório do texto\n'
                    '0 - Sair\n'
                    f'{"-" * 50}\n'
                    f'')
    with open('textos.txt', 'a+', encoding='utf-8') as arquivo:
        if escolha == '1':
            print('Para parar de escrever, escreva uma linha com a palavra "sair')
            while True:
                texto_usuario = input(f'Digite a linha: ')
                if texto_usuario == 'sair':
                    break
                else:
                    arquivo.write(f"{texto_usuario}\n")
        elif escolha == '2':
            arquivo.seek(0, 0)
            print(arquivo.read())
        elif escolha == '3':
            arquivo.seek(0, 0)
            linhas = contar_linhas(arquivo)
            arquivo.seek(0, 0)
            all_caracters = len(arquivo.read()) - linhas
            esp = contar_espacos(arquivo)
            print(f'RELATÓRIO GERADO COM SUCESSO!\n'
                  f'Número de linhas = {linhas}\n'
                  f'Quantidade total de caracteres = {all_caracters}\n'
                  f'Quantidade de espaços = {esp}')
        elif escolha == '0':
            print('Encerrado')
            break
        else:
            print('Digite algo válio...')
