from cliente import Cliente
from conta import Conta
from datas import Data

conta1 = Conta("1001", "Fulano de Tal", 100.0, 1000.0)
conta2 = Conta("1002", "Bel Trano", 200.0, 1000.0)

conta1.sacar(25000.0)

codigo_do_banco = Conta.codigos_do_bancos()
print(codigo_do_banco["Itaú"])

data = Data(1, 11, 1920)
data.formatada()

cliente = Cliente("ciclano")
print(cliente.nome)
cliente.nome = "mengano"
print(cliente.nome)
