"""Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com
 a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a
 taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um
 programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o
 método adicioneJuros() cinco vezes e imprime o saldo resultante."""

import time


class ContaInvestimento:
    def __init__(self, numero_da_conta, nome, saldo=0, taxa_de_juros=0.1):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = saldo
        self.juros = taxa_de_juros

    def adicioneJuros(self):
        self.saldo += self.saldo * self.juros

    def alterarnome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, dinheiro_depositado):
        self.saldo = self.saldo + dinheiro_depositado

    def saque(self, saque):
        self.saldo = self.saldo - saque
        if self.saldo < 0:
            self.saldo = 0


conta = ContaInvestimento(900, 'jonathas', 1000, 0.1)
print(f'Saldo atual {conta.saldo:.2f}R$')
print('Aplicando juros...')
for p in range(5):
    time.sleep(0.5)
    conta.adicioneJuros()
    print('.')
print(f'Juros em 5x aplicado')
print(f'Saldo atual {conta.saldo:.2f}R$')
