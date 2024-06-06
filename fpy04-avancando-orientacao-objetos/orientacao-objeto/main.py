from modulo import Filme, Serie

filme = Filme("Vingadores - Guerra Infinita", 2018, 160)
filme.like()
print(f"Nome: {filme.nome}, Ano: {filme.ano}, Duração: {filme._duracao}, likes: {filme.likes}")

serie = Serie("Atlanta", 2018, 2)
serie.like()
print(f"Nome: {serie.nome}, Ano: {serie.ano}, Temporadas: {serie._temporadas}, likes: {serie._likes}")
