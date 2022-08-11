def mostrar_tarefas(lista):
    print('Tarefas: ')
    print(lista)


tarefas = []
guardar = []
while True:
    escolha = input('1 - Adicionar 2 - Desfazer 3 - Refazer 4 - Listar 0 - Sair: ')
    if escolha == '1':
        tarefa_a_ser_add = input('Digite o nome da tarefa: ')
        tarefas.append(tarefa_a_ser_add)
        guardar.append(tarefa_a_ser_add)
    elif escolha == '2':
        try:
            tarefas.pop()
        except:
            print('Nada a desfazer')
    elif escolha == '3':
        for p in guardar:
            if p in tarefas:
                continue
            else:
                tarefas.append(p)
                break
    elif escolha == '4':
        mostrar_tarefas(tarefas)
    elif escolha == '0':
        break
    else:
        print('Digite algo válido...')
