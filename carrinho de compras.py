carrinho = []
carrinho.append(('Camisa', 25))
carrinho.append(('Camisa', 30))
carrinho.append(('Camisa', 50))
total = sum([preco for produto, preco in carrinho])
print(total)
