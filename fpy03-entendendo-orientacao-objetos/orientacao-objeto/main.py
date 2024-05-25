from conta import Conta

conta = Conta("1001", "Fulano de Tal", 100.0, 1000.0)
conta.consultar_extrato()
conta.depositar(200.0)
conta.consultar_extrato()
conta.sacar(50.0)
conta.consultar_extrato()
