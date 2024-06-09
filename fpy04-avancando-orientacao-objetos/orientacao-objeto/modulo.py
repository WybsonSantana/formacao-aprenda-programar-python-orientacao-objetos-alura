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
