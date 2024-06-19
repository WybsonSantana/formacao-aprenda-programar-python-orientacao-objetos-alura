from conta import ContaCorrente, ContaPoupanca

conta16 = ContaCorrente(16)
conta16.depositar(1000)
conta16.passar_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.depositar(1000)
conta17.passar_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.depositar(1000)
conta17 = ContaPoupanca(17)
conta17.depositar(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passar_mes()  # duck typing
    print(conta)
