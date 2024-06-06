class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

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
        self._nome = nome.title()
        self._ano = ano
        self._duracao = duracao
        self._likes = 0


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self._ano = ano
        self._temporadas = temporadas
        self._likes = 0
