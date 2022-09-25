import os

caminho_a_pesquisar = input(f'Digite o caminho em que deseja vasculhar: ')
termo_a_pesquisar = input(f'Digite o termo que deseja pesquisar: ')


def formatar(tamanho_a_formatar):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if tamanho_a_formatar < kilo:
        texto = 'B'
    elif tamanho_a_formatar < mega:
        tamanho_a_formatar /= kilo
        texto = 'k'
    elif tamanho_a_formatar < giga:
        tamanho_a_formatar /= mega
        texto = 'M'
    elif tamanho_a_formatar < tera:
        tamanho_a_formatar /= giga
        texto = 'G'
    elif tamanho_a_formatar < peta:
        tamanho_a_formatar /= tera
        texto = 'T'
    else:
        texto = 'P'
    tamanho_a_formatar = round(tamanho_a_formatar, 2)
    return f'{tamanho_a_formatar} {texto}'


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_a_pesquisar):
    for arq in arquivos:
        if termo_a_pesquisar in arq:
            try:
                caminho_full = os.path.join(raiz, arq)
                nome_arq, ext_arq = os.path.splitext(arq)
                tamanho = os.path.getsize(caminho_full)

                print('#' * 50)
                print(f'Arquivo encontrado!\n'
                      f'Caminho: {caminho_full}\n'
                      f'Nome: {nome_arq}\n'
                      f'Extensão: {ext_arq}\n'
                      f'Tamanho: {tamanho}\n'
                      f'Tamanho formatado: {formatar(tamanho)}')
                print('#' * 50)
                print()
                conta += 1
            except PermissionError as e:
                print('Sem permissão.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido')
print()
print(f'{conta} aquivos encontrados')
