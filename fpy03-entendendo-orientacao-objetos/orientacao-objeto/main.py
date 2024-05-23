import teste
from teste import depositar, sacar, extrato

conta = teste.criar_conta("1001", "Fulano de Tal", 100.0, 1000.0)

depositar(conta, 300.0)
sacar(conta, 150.0)
extrato(conta)
