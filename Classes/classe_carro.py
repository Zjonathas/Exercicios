"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( )"""


class Carro:
    def __init__(self, cosumo):
        self.cosumo = cosumo
        self.combustivel = 0

    def andar(self, km):
        resultado = self.combustivel - (km / self.cosumo)
        self.combustivel = self.combustivel - resultado
        return resultado

    def get_gasolina(self):
        return self.combustivel

    def set_gasolina(self, qtd):
        self.combustivel = self.combustivel + qtd
        return self.combustivel


carro = Carro(15)
carro.set_gasolina(35)
print(f'O carro está com {carro.get_gasolina():.2f} de combustível.')
print(f'O carro andou 100km e gastou {carro.andar(100):.2f}')
print(f'O carro está com {carro.get_gasolina():.2f} de combustível.')
