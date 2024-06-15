class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._likes} Like(s)'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, novo_ano):
        self._ano = novo_ano

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._duracao} minuto(s) - {self._likes} Like(s)'

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self._ano} - {self._temporadas} temporada(s) - {self._likes} Like(s)'

    @property
    def temporadas(self):
        return self._temporadas


class Playlist:

    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def nome(self):
        return self._nome


# Herança múltipla
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass