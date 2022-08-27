"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os
métodos comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os
com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?"""


class Macaco:
    def __init__(self, nome, bucho=''):
        self.nome = nome
        self.bucho = bucho

    def comer(self, comida):
        if isinstance(comida, str):
            self.bucho += f', {comida}'
            return
        return f'{self.nome} não pode comer {comida}'

    def ver_bucho(self):
        if self.bucho == '':
            return f'{self.nome} está de bucho vazio'
        return f'{self.nome} está com {self.bucho} no bucho'

    def digerir(self):
        if self.bucho == '':
            return f'{self.nome} não tem o que digerir...'
        self.bucho = ''
        return f'{self.nome} digeriu a comida'


macaco1 = Macaco('José', 'Banana')
macaco2 = Macaco('Alisson', 'Maçã')
macaco1.comer('maçã')
macaco1.comer('arroz')
macaco2.comer('mamão')
macaco2.comer('kiwi')
macaco1.comer(macaco2)
print(f'{macaco1.ver_bucho()}')
print(f'{macaco1.ver_bucho()}, {macaco2.ver_bucho()}')
print(f'{macaco1.ver_bucho()}, {macaco2.digerir()}')
