"""Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve
criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local."""


class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_tamanho_altura(self, novo_lado_a):
        self.lado_a = novo_lado_a

    def mudar_tamanho_base(self, novo_lado_b):
        self.lado_b = novo_lado_b

    def mostrar_valor_do_lado(self):
        print(f'Valor do lado 1: {self.lado_a} \nValor do lado 2: {self.lado_b}')

    def calcular_area(self):
        area = self.lado_a * self.lado_b
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.lado_b + self.lado_b)
        return perimetro


retangulo = Retangulo(2, 2)
print(f'Area: {retangulo.calcular_area()}')
print(F'Perimetro {retangulo.calcular_perimetro()}')
retangulo.mostrar_valor_do_lado()
retangulo.mudar_tamanho_altura(3)
retangulo.mostrar_valor_do_lado()
print(f'Area: {retangulo.calcular_area()}')

lado1 = float(input('Digite o comprimento do local: '))
lado2 = float(input('Digite a base do local: '))
lugar = Retangulo(lado1, lado2)

print(f'Serão necessários {lugar.calcular_area()}m² de pisos e {lugar.calcular_perimetro()}m de rodapés')
