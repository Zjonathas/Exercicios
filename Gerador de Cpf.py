from random import randint
numero = str(randint(100000000, 999999999))

contrario = 10
total = 0
new_CPF = numero
for posicao in range(19):
    if posicao > 8:
        posicao -= 9
    total += int(new_CPF[posicao]) * contrario
    contrario -= 1
    if contrario < 2:
        contrario = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        total = 0
        new_CPF += str(d)
print(new_CPF)
