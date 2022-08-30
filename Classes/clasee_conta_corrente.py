"""Classe Conta Corrente: Crie uma classe para implementar uma conta-corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""


class ContaCorrente:
    def __init__(self, numero_da_conta, nome, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = saldo

    def alterarnome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, dinheiro_depositado):
        self.saldo = self.saldo + dinheiro_depositado

    def saque(self, saque):
        self.saldo = self.saldo - saque
        if self.saldo < 0:
            self.saldo = 0
