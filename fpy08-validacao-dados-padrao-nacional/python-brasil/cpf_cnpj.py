from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def criar_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")


class DocCpf:

    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formatar()

    def validar(self, cpf):
        documento = CPF()
        return documento.validate(cpf)

    def formatar(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.formatar()

    def validar(self, cnpj):
        documento = CNPJ()
        return documento.validate(cnpj)

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
