from zipfile import ZipFile
import os


while True:
    escolha = input('Escolha uma opção:\n'
                    '1 - Compactar\n'
                    '2 - Descompactar\n'
                    '0 - Sair')
    if escolha == '1':
        caminho = input('Digite o caminho: ')
        with ZipFile('arq.zip', 'w') as zipp:
            for arquivo in os.listdir(caminho):
                caminho_full = os.path.join(caminho, arquivo)
                zipp.write(caminho_full, arquivo)
        with ZipFile('arq.zip', 'r') as zipp:
            for arquivo in zipp.namelist():
                print(arquivo)

    elif escolha == '2':
        with ZipFile('arq.zip', 'r') as zipp:
            zipp.extractall('descompactado')

    else:
        print('Finalizado')
        break

