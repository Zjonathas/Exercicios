import random
while True:
    palpite = int(input('Dê um palpite de 0 a 10: '))
    if palpite < 0 or palpite > 10:
        print('Inválido')
        continue
    numero = random.randint(0, 10)
    diferenca = abs(palpite - numero)
    if palpite == numero:
        print('Acertou, parabéns.... Encerrando')
        break
    elif diferenca <= 2:
        print('Passou perto')
        print(f'O número era {numero}')
    elif diferenca > 2:
        print('Passou longe')
        print(f'O número era {numero}')
