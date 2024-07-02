from bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_17_03_2000_deve_retornar_24(self):
        entrada = '17/03/2000'
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1500)
        resultado = funcionario_teste.idade()

        assert resultado == esperado
