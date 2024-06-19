class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


print(Conta(88))


class ContaCorrente(Conta):

    def passar_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passar_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3
