from conta import ContaCorrente, ContaPoupanca, ContaSalario, Conta
from operator import attrgetter
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

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)

print(conta1 == conta2)

isinstance(ContaCorrente(34), ContaCorrente)

isinstance(ContaCorrente(34), Conta)

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

range(len(idades))  # lazy...

enumerate(idades)  # lazy

list(range(len(idades)))  # forcei a geração dos valores

list(enumerate(idades))

for indice, idade in enumerate(idades):  # unpacking da nossa tupla
    print(indice, 'x', idade)

usuarios = [
    ('Fulano', 37, 1981),
    ('Beltrano', 31, 1987),
    ('Ciclano', 39, 1979)
]

for nome, idade, nascimento in usuarios:  # ja desempacotando
    print(nome)

for nome, _, _ in usuarios:  # ja desempacotando, ignorando o resto
    print(nome)

idades = [40, 28, 19, 21, 90, 52, 45]

print(sorted(idades))

print(15 < 32)

print(list(reversed(idades)))

print(sorted(idades, reverse=True))

print(list(reversed(sorted(idades))))

print(idades)

idades.sort()

print(idades)

conta_do_fulano = ContaSalario(17)
conta_do_fulano.depositar(500)

conta_do_beltrano = ContaSalario(3)
conta_do_beltrano.depositar(1000)

conta_do_ciclano = ContaSalario(133)
conta_do_ciclano.depositar(510)

contas = [conta_do_fulano, conta_do_beltrano, conta_do_ciclano]

for conta in contas:
    print(conta)

sorted(contas)

print(conta_do_fulano < conta_do_beltrano)


def extrai_saldo(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo):
    print(conta)

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)
