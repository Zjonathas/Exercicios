"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
1 - tipoCombustivel.
2 - valorLitro
3 - quantidadeCombustivel
Possua no mínimo esses métodos:
4 - abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade
de litros que foi colocada no veículo
5 - abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra
o valor a ser pago pelo cliente.
6 - alterarValor( ) – altera o valor do litro do combustível.
7 - alterarCombustivel( ) – altera o tipo do combustível.
8 - alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""


class BombaDeCombustivel:
    def __init__(self, tipo, valor_litro, quantidade):
        self.tipo = tipo
        self.valor_litro = valor_litro
        self.quantidade = quantidade

    def abastecer_por_valor(self, dinheiro):
        resultado = dinheiro / self.valor_litro
        self.quantidade = self.quantidade - resultado
        return resultado

    def abastecer_por_litro(self, litros):
        resultado2 = litros * self.valor_litro
        self.quantidade = self.quantidade - resultado2
        return resultado2

    def alterar_valor(self, new_value):
        self.valor_litro = new_value

    def alterar_combustivel(self, new_combus):
        self.tipo = new_combus

    def alterar_quantidade(self, new_amount):
        self.quantidade = new_amount


bomba = BombaDeCombustivel('gasolina', 4.19, 100)
print(f'Na bomba ainda tem {bomba.quantidade}L de {bomba.tipo}')
print(f'8.38R$ deu para {bomba.abastecer_por_valor(8.38)} litro(s) de {bomba.tipo}')
print(f'Na bomba ainda tem {bomba.quantidade}L de {bomba.tipo}')
print(f'7 litros de {bomba.tipo} ficou no valor de {bomba.abastecer_por_litro(7):.2f}R$')
print(f'Na bomba ainda tem {bomba.quantidade}L de {bomba.tipo}')
