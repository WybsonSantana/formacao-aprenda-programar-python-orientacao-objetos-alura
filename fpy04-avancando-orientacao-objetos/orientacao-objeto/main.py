from modulo import Filme, Serie

filme = Filme("Vingadores - Guerra Infinita", 2018, 160)
filme.like()
print("{filme.nome} - {filme.duracao}: {filme.likes}")

serie = Serie("Atlanta", 2018, 2)
serie.like()
print("{serie.nome} - {serie.temporadas}: {serie.likes}")
