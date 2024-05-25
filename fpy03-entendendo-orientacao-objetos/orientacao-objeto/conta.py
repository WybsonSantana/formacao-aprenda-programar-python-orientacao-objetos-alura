class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def consultar_extrato(self):
        print("Saldo de R$ {:.2f} do titular {}.".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("Depósito de R$ {:.2f} realizado com sucesso!".format(valor))

    def sacar(self, valor):
        self.__saldo -= valor
        print("Saque de R$ {:.2f} realizado com sucesso!".format(valor))

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)
