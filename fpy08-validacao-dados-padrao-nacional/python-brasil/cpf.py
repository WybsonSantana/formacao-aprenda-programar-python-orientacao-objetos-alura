class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formatar_cpf()

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def formatar_cpf(self):
        fatia1 = self.cpf[:3]
        fatia2 = self.cpf[3:6]
        fatia3 = self.cpf[6:9]
        fatia4 = self.cpf[9:]

        return f'{fatia1}.{fatia2}.{fatia3}-{fatia4}'
