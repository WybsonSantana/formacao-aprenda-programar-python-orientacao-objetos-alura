class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def consultar_extrato(self):
        print("Saldo de R$ {:.2f} do titular {}.".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$ {:.2f} realizado com sucesso!".format(valor))

    def sacar(self, valor):
        self.saldo -= valor
        print("Saque de R$ {:.2f} realizado com sucesso!".format(valor))
