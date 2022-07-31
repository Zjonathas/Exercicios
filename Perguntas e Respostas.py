pergunta = {'Pergunta 1': {'pergunta': 'Quanto é 1+1?',
                           'resposta': {'[a]': 2, '[b]': 3, '[c]': 4},
                           'resposta_certa': 'a'},
            'Pegunta 2': {'pergunta': 'Quanto é 2*2?',
                          'resposta': {'[a]': 2, '[b]': 3, '[c]': 4},
                          'resposta_certa': 'c'},
            'Pegunta 3': {'pergunta': 'Quanto é 4²?',
                          'resposta': {'[a]': 16, '[b]': 15, '[c]': 8},
                          'resposta_certa': 'a'},
            'Pegunta 4': {'pergunta': 'Quanto é 2³?',
                          'resposta': {'[a]': 10, '[b]': 6, '[c]': 8},
                          'resposta_certa': 'c'},
            'Pegunta 5': {'pergunta': 'Quanto é 10/5?',
                          'resposta': {'[a]': 25, '[b]': 4, '[c]': 2},
                          'resposta_certa': 'c'},
            'Pegunta 6': {'pergunta': 'Quanto é 10³?',
                          'resposta': {'[a]': 100, '[b]': 1000, '[c]': 30},
                          'resposta_certa': 'b'},
            }
respotas_corretas = 0
for pk, pv in pergunta.items():
    print('#' * 50)
    print(f'{pk}: {pv["pergunta"]}')
    print()
    print('Escolha uma das opções a baixo')
    print()
    for rk, rv in pv['resposta'].items():
        print(f'{rk}: {rv}')
        print()
    escolha = input('Digite a resposta: ')
    if escolha == pv['resposta_certa']:
        print('AEEEEEE, a resposta correta era essa mesmo')
        respotas_corretas += 1
    else:
        print(f'VISHHHHHHH, você errou! A resposta certa era a letra ({pv["resposta_certa"]})')

qtd_de_perguntas = len(pergunta)

porcentagem = respotas_corretas / qtd_de_perguntas * 100

print(f'Você acertou {respotas_corretas} respostas')
print(f'A porcentagem de acerto foi de {porcentagem}%')
