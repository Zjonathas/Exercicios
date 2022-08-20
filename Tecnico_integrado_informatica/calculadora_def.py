"""Escreva um programa que apresente o menu de opções abaixo. Para cada uma das
opções crie um método para executar a ação especificada. Escreva uma mensagem de
erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números
3- Produto entre 2 números.
4- Divisão entre 2 números*
0 – Sair**
* A divisão de um número por zero dispara um erro. Trate esse problema na função
** o programa deve permanecer em execução enquanto o usuário não digitar zero"""


def soma(x, y):
    return x + y


def diferenca(x, y):
    return x - y


def produto(x, y):
    return x * y


def razao(x, y):
    if y == 0:
        return print('Não é possivel divir por 0')
    return x / y


while True:
    escolha = input('1- Soma de 2 números.\n'
                    '2- Diferença entre 2 números.\n'
                    '3- Produto entre 2 números.\n'
                    '4- Divisão entre 2 números.\n'
                    '0 – Sair.\n')
    if escolha == '1':
        x = float(input('Digite um número: '))
        y = float(input('Digite o segundo número: '))
        print(soma(x, y))
    elif escolha == '2':
        x = float(input('Digite um número: '))
        y = float(input('Digite o segundo número: '))
        print(diferenca(x, y))
    elif escolha == '3':
        x = float(input('Digite um número: '))
        y = float(input('Digite o segundo número: '))
        print(produto(x, y))
    elif escolha == '4':
        x = float(input('Digite um número: '))
        y = float(input('Digite o segundo número: '))
        print(razao(x, y))
    elif escolha == '0':
        break
    else:
        print('Digite algo válido...')
