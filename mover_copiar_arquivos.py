import os
import shutil

caminho_original = r''
caminho_novo = r''
try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    # print(f'A pastra {caminho_novo} já existe.')
    pass

for raiz, dire, arqs in os.walk(caminho_original):
    for arq in arqs:
        caminho_antigo = os.path.join(raiz, arq)
        novo_cam = os.path.join(caminho_novo, arq)

        shutil.move(caminho_antigo, novo_cam)
        print(f'Arquivo {arq} foi movido com sucesso.')