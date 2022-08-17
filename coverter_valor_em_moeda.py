"""Crie uma função que recebe um determinado valor em reais, calcula e retorna esse valor
convertido em moedas de R$ 1.00, R$ 0.50, R$ 0.25, R$ 0.10, R$ 0.05 e R$ 0.01. Por
exemplo, R$ 3.78 resulta em três moedas de um real, uma de cinquenta centavos, duas
de dez centavos, uma de 5 centavos e três de um centavo."""


def converter(valor):
    valores = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = 0
    lista = []
    for p in valores:
        while True:
            resultado += p
            lista.append(p)
            if resultado > valor:
                resultado -= p
                lista.pop()
                break

    print(f'O dinheiro ficou assim {lista}')


converter(3.78)
