from validate_docbr import CPF, CNPJ


class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento.lower() == 'cpf':
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido")
        elif self.tipo_documento.lower() == 'cnpj':
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.formatar_cpf()

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            documento = CPF()
            return documento.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            documento = CNPJ()
            return documento.validate(cnpj)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def formatar_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
