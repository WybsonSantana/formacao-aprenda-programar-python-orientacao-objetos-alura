from conta import Conta
from datas import Data

conta1 = Conta("1001", "Fulano de Tal", 100.0, 1000.0)
conta2 = Conta("1002", "Bel Trano", 200.0, 1000.0)

conta1.consultar_extrato()
conta2.consultar_extrato()

conta1.transferir(50.0, conta2)
conta1.consultar_extrato()
conta2.consultar_extrato()

conta1.set_limite(2000.0)
print("Limite da conta de {}: R$ {:.2f}".format(conta1.get_titular(), conta1.get_limite()))

data = Data(1, 11, 1920)
data.formatada()
