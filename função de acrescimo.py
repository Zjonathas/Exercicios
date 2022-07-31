def percentual(valor, porcento):
    porcento = porcento / 100
    valor = valor + (porcento * valor)
    return valor


juros = float(input('Digite a porcentagem: '))
dinheiro = float(input('Digite o valor: '))
print(f'O valor de {dinheiro:.2f}R$ com acrescimo de {juros}% ficou {percentual(dinheiro, juros):.2f}R$')
