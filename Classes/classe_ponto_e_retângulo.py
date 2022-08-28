"""Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um
objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo."""


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro(self):
        centro_x = (self.largura.x + self.altura.x) / 2
        centro_y = (self.largura.y + self.altura.y) / 2
        return f'x = {centro_x} e y = {centro_y}'


def imprimir(args, kwargs):
    if args == 0:
        print('0, 0')
        return
    print(f"X = {args.x} | Y = {args.y}")


retangulo = Retangulo(0, 0)
canto_1 = 0
canto_2 = 0

while True:

    print('-' * 50)
    escolha = input(f'1 - Imprimir valores do ponto\n2 - Alterar valores\n3 - Imprimir centro\nQUALQUER OUTRA'
                    f'COISA PARA SAIR\n{"-" * 50}\n')
    if escolha == '1':
        imprimir(canto_1, canto_2)
    elif escolha == '2':
        x_valor1 = float(input('Digite a coordenada x do canto inferior esquerdo: '))
        y_valor1 = float(input('Digite a coordenada y do canto inferior esquerdo: '))
        canto_1 = Ponto(x_valor1, y_valor1)
        x_valor2 = float(input('Digite a coordenada x do canto superior direito: '))
        y_valor2 = float(input('Digite a coordenada y do canto superior direito: '))
        canto_2 = Ponto(x_valor2, y_valor2)
        retangulo = Retangulo(canto_1, canto_2)
    elif escolha == '3':
        print(retangulo.centro())
    else:
        break
