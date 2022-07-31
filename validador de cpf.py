contrario = 10
total = 0
while True:
    escolha = input('Quer para o progama? Digite 1 para sim e 2 para não: ')
    if escolha == '1':
        break
    else:
        cpf = input('Digite um CPF: ')
        cpf_sem_os_digitos = cpf[:-2]
        for posicao in range(19):
            if posicao > 8:
                posicao -= 9
            total += int(cpf_sem_os_digitos[posicao]) * contrario
            contrario -= 1
            if contrario < 2:
                contrario = 11
                d = 11 - (total % 11)
                if d > 9:
                    d = 0
                total = 0
                cpf_sem_os_digitos += str(d)

        if cpf == cpf_sem_os_digitos:
            print(f'O CPF {cpf} é VÁLIDO ')
            contrario = 10
            continue
        else:
            print(f'O CPF {cpf} é INVÁLIDO ')
            contrario = 10
