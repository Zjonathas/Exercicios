"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(f'Cor: {self.cor}')


bola = Bola('Azul', 13, 'Couro')
bola.mostraCor()
bola.trocaCor('Vermelho')
bola.mostraCor()
