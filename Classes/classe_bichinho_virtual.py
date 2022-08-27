"""Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um
atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento."""


class BichinhoVirtual:
    def __init__(self, nome, fome, idade):
        self._nome = nome
        self.idade = idade
        self.fome = fome
        self.saude = 100
        self.humor = ''

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        if isinstance(name, str):
            self._nome = name

    def alterar_fome(self, new_fome):
        self.fome = new_fome
        return

    def alterar_saude(self, new_saude):
        self.saude = new_saude

    def alterar_idade(self, new_age):
        self.idade = new_age
        return

    def get_humor(self):
        if self.saude >= 70 and self.fome >= 70:
            return f'{self.nome} está feliz e bem'
        elif self.saude <= 25 and self.fome >= 70:
            return f'{self.nome} está feliz porque está cheio, mas não esta com a saúde boa'
        elif self.saude >= 70 and self.fome <= 25:
            return f'{self.nome} está bem de saúde, mas não está muito feliz devido a está de barriga vazia'
        elif self.saude <= 25 and self.fome <= 25:
            return f'{self.nome} não está nada bem...'
        else:
            return f'{self.nome} está +/-'


