def numero_duplicado(lista):
    checks = set()
    primeiro_chekc = -1
    for num in lista:
        if num in checks:
            primeiro_chekc = num
            break
        checks.add(num)
    return primeiro_chekc


inteiros = [[1, 2, 3, 5, 3, 2, 5, 7, 4, 10, ],
            [2, 3, 5, 4, 2, 2, 3, 4, 9, 10, ],
            [4, 4, 5, 7, 8, 9, 0, 10, 9, 8, ],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ], ]
for lista_int in inteiros:
    print(lista_int, numero_duplicado(lista_int))
