from validate_docbr import CPF


class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formatar_cpf()

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            documento = CPF()
            return documento.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def formatar_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
