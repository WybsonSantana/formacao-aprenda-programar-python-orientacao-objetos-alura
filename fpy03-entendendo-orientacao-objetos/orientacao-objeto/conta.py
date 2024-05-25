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

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, novo_limite):
        self.__limite = novo_limite
