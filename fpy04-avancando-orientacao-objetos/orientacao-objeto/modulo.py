class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao = nova_duracao

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def temporadas(self):
        return self.__temporadas

    @temporadas.setter
    def temporadas(self, nova_temporada):
        self.__temporadas = nova_temporada

    @property
    def likes(self):
        return self.__likes

    def like(self):
        self.__likes += 1
