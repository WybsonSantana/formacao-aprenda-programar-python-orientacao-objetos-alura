from conta import ContaCorrente, ContaPoupanca
import array as arr
import numpy as np

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
    conta.passar_mes()
    print(conta)

arr.array('d', [1, 3.5])
# arr.array('d', [1, 3.5, 'Fulano'])

numeros = np.array([1, 3.5])
print(numeros)
print(numeros + 3)
