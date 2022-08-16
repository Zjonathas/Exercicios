"""Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo
a idade dela menor que 21 anos, ela deve crescer 0,5 cm."""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        resultado_do_crescimento = 0
        soma = self.idade + anos
        if soma <= 21:
            resultado_do_crescimento = anos * 0.5
        # if self.idade < 21:
        #     if self.idade + anos > 21:
        #         resultado_do_crescimento = ((21 - self.idade) * 0.5)
        self.idade += anos
        print(f'{self.nome} agora está com {self.idade} anos de idade e ')
        self.crescer(resultado_do_crescimento)

    def engordar(self, kilos):
        self.peso += kilos
        print(f'{self.nome} engordou {kilos}kg e agora está pesando {self.peso:.2f}kg')

    def emagrecer(self, kilos):
        self.peso -= kilos
        print(f'{self.nome} emagreceu {kilos}kg e agora está pesando {self.peso:.2f}kg')

    def crescer(self, cm):
        self.altura += cm
        print(f'{self.nome} cresceu {cm}cm e agora tem {self.altura / 100:.2f}m')


pessoa = Pessoa('Jonathas', 17, 75, 180)

pessoa.envelhecer(4)
pessoa.engordar(10)
pessoa.emagrecer(12)
pessoa.crescer(10)
