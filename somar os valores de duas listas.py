lista_a = [3, 4, 10, 90, 9]
lista_b = [1, 2, 3, 4, ]
soma = zip(lista_a, lista_b)
soma_ofc = [(x + y) for x, y in soma]
print(list(soma_ofc))
