string = '012345678901234567890123456789012345678901234567890123456789'
lista = [variavel if variavel != '9' else '.' for variavel in string]

print(''.join(lista))