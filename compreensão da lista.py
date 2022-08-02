string = '012345678901234567890123456789012345678901234567890123456789'
lista = [string[variavel:variavel + 10] for variavel in range(0, len(string), 10)]

print('.'.join(lista))