from modulo import Filme, Serie

filme = Filme("Vingadores - Guerra Infinita", 2018, 160)
filme.like()

serie = Serie("Atlanta", 2018, 2)
serie.like()

filmes_e_series = [filme, serie]

for programa in filmes_e_series:
    programa.imprimir()
