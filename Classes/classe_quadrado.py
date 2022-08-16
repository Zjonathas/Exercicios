"""Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;"""


class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.lado = tamanho_do_lado

    def mudar_valo_do_lado(self, novo_valor):
        self.lado = novo_valor

    def mostrar_valor_do_lado(self):
        return self.lado

    def calcular_area(self):
        print(f'Area: {self.lado * 4}')


quadrado = Quadrado(4)
quadrado.calcular_area()
print(f'Lado: {quadrado.mostrar_valor_do_lado()}')
quadrado.mudar_valo_do_lado(2)
print(f'Lado: {quadrado.mostrar_valor_do_lado()}')
