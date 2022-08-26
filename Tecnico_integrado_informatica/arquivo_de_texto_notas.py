def percorre_arq():
    alunos_notas = []
    with open('notas.txt', 'a+', encoding='utf-8') as arq:
        arq.seek(0)
        for linha in arq:
            alunos_notas.append(linha.split())
    return alunos_notas


def calcular_media(nota):
    media = sum(nota) / len(nota)
    return media


def calcular_diferenca(notas, media):
    diferencas = []
    for ele in notas:
        diferenca = ele - media
        diferencas.append(f'{diferenca:.2f}')
    return diferencas


def relatorio():
    lista_pronta = percorre_arq()
    acima_media = 0
    abaixo = 0
    aluno_e_nota = []
    notas = []
    contador = 0
    print('-' * 50)
    for elemento in lista_pronta:
        notas.append(float(elemento[1]))
        aluno_e_nota.append(elemento)
    media_temp = calcular_media(notas)
    difs = calcular_diferenca(notas, media_temp)
    for p in aluno_e_nota:
        print(f'Aluno: {p[0]} | Nota: {p[1]} | Dif: {difs[contador]}')
        if float(difs[contador]) >= 0:
            acima_media += 1
        elif float(difs[contador]) < 0:
            abaixo += 1
        contador += 1

    print('-' * 50)
    print(f'Media: {media_temp:.2f}')
    print(f'Acima da média: {acima_media} \nAbaixo da média: {abaixo}')


def procurar(mat):
    with open('notas.txt', 'a+', encoding='utf-8') as arquivooo:
        arquivooo.seek(0)
        aluno_temp = []
        for al in arquivooo:
            aluno_temp.append(al.split())
            if mat not in al.split():
                continue
            else:
                return al.split()


with open('notas.txt', 'a+', encoding='utf-8') as arquivo:
    escolha = input('1 - Exibir relatório | 2 - Exibir notas | 3 - Add aluno | 4 - PROCUAR')
    if escolha == '2':
        lista_pronta = percorre_arq()
        for elemento in lista_pronta:
            print(f'Aluno: {elemento[0]} Nota {elemento[1]}')
    elif escolha == '1':
        relatorio()
    elif escolha == '3':
        matricula = input('Digite a matricúla: ')
        nota_add = input('Digite a nota: ')
        arquivo.write(f'{matricula} {nota_add}\n')
    elif escolha == '4':
        matricula = input('Digite a matricúla: ')
        achado = procurar(matricula)
        notas = []
        lista_pronta = percorre_arq()
        for elemento in lista_pronta:
            notas.append(float(elemento[1]))
        media_temp = calcular_media(notas)
        print(f'Aluno: {achado[0]} | Nota: {achado[1]} | Dif: {float(achado[1]) - media_temp:.2f}')
        if float(achado[1]) - media_temp < 0:
            print('Abaixo da media')
        else:
            print('Acima')
