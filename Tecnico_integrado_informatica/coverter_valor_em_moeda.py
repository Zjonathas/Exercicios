"""Crie uma função que recebe um determinado valor em reais, calcula e retorna esse valor
convertido em moedas de R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01. Por
exemplo, R$ 3.78 resulta em três moedas de um real, uma de cinquenta centavos, duas
de dez centavos, uma de 5 centavos e três de um centavo."""


def converter(valor):
    resultao_parcial = ''
    resultao_parcial2 = ''
    valores = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = 0
    lista = []
    imprimir = []
    for p in valores:
        while True:
            resultado += p
            lista.append(p)
            if resultado > valor:
                resultado -= p
                lista.pop()
                teste = p
                if teste > 0.50:
                    resultao_parcial = f'{len(lista)} moeda(s) de {teste} real\n'
                    imprimir.append(resultao_parcial)
                    lista = []
                else:
                    if len(lista) == 0:
                        break
                    else:
                        resultao_parcial2 = f'{len(lista)} moeda(s) de {teste} centavos\n'
                        imprimir.append(resultao_parcial2)
                        lista = []
                break

    print(f'Você precisará de: \n {" ".join(imprimir)}')


converter(3.78)
