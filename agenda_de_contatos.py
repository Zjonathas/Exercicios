import colorama
lista_qtd = []
contato = open('Agenda.txt', 'a', encoding='utf-8')
while True:
    escolha = input('Quer adicionar um contato a agenda ou deseja sair? [sim] para sim, [sair] sair e [listar]'
                    'para ver como está a sua agenda: ')
    if escolha == 'listar':
        contato.close()
        with open('Agenda.txt', 'r', encoding='utf-8') as lista:
            for qtd in lista:
                lista_qtd.append(qtd)
        if len(lista_qtd) == 0:
            print(colorama.Fore.RED + 'Sua agenda está vazia')
            print(colorama.Fore.RESET)
            continue
        else:
            with open('Agenda.txt', 'r', encoding='utf-8') as lista:
                print()
                print('#' * 50)
                print(colorama.Fore.BLUE + f'Esta é sua agenda: ')
                print(colorama.Fore.GREEN + f'{lista.read()}')
                print(colorama.Fore.RESET + '#' * 50)
                continue
    elif escolha == 'sim':
        contato_a_adicionar = input('Digite o nome da pessoa a ser adicionada na agenda: ')
        email_a_adicionar = input('Digite o email: ')
        numero_a_adicionar = input('Digite o número: ')
        contato.write(f'|Nome: {contato_a_adicionar}| ')
        contato.write(f'|Email: {email_a_adicionar}|')
        contato.write(f'Número: {numero_a_adicionar}|\n')
    elif escolha == 'sair':
        break
    else:
        print('Digite algo válido...')
