"""Exercício com Abstração, Herança, Encapsulamento e Polimorfismo Criar um sistema bancário (extremamente simples) que
tem clientes, contas e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas.
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
Pessoa tem nome e idade (com getters)
Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca) Criar classes ContaPoupanca e ContaCorrente
que herdam de Conta
Contas têm agência, número da conta e saldo Contas devem ter método para depósito
ContaCorrente deve ter um limite extra Conta (super classe) deve ter o método sacar abstrato
(Abstração e polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação) Banco será responsável autenticar
o cliente e as contas da seguinte maneira:
Banco tem contas e clentes (Agregação)
* Checar se a agência é daquele banco
*Checar se o cliente é daquele banco
* Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)"""

from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @property
    def nome(self):
        return self._nome


class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def relatorio(self):
        print(f'{"-" * 50}\nAgência: {self.agencia}\nNúmero da conta: {self.numero_da_conta}\nSaldo: {self.saldo}\n'
              f'{"-" * 50}\n')

    def deposito(self, valor):
        self.saldo += valor
        self.relatorio()

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.relatorio()


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite=200):
        super().__init__(agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.relatorio()


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def setar_conta(self, conta):
        self.conta = conta


class Banco:
    def __init__(self):
        self.agencia = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)

    def inserir_contas(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencia:
            return False
        return True


banco = Banco()
cliente1 = Cliente('Jonathas', 17)
cliente2 = Cliente('Mikaelle', 18)
cliente3 = Cliente('Suerda', 41)

conta1 = ContaPoupanca(1111, 109286, 0)
conta2 = ContaCorrente(2222, 209286, 0)
conta3 = ContaPoupanca(3333, 309286, 0)

cliente1.setar_conta(conta1)
cliente2.setar_conta(conta2)
cliente3.setar_conta(conta3)

banco.inserir_contas(conta1)
banco.inserir_clientes(cliente1)
banco.inserir_contas(conta2)
banco.inserir_clientes(cliente2)
if banco.autenticar(cliente1):
    cliente1.conta.deposito(20)
    cliente1.conta.sacar(20)
else:
    print(f'Cliente não autenticado')

print('#' * 50)
if banco.autenticar(cliente2):
    cliente2.conta.sacar(20)
else:
    print(f'Cliente não autenticado')
