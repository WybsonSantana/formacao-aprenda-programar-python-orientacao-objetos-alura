from bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_17_03_2000_deve_retornar_24(self):
        entrada = '17/03/2000'
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1500)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_nome_recebe_bel_trano_deve_retornar_trano(self):
        entrada = 'Bel Trano'
        esperado = 'Trano'

        funcionario_teste = Funcionario(entrada, 15 / 11 / 1995, 2000)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperado
