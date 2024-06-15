from modulo import Filme, Serie, Playlist

vingadores_guerra_infinita = Filme("Vingadores - Guerra Infinita", 2018, 160)
todo_mundo_em_panico = Filme("Todo Mundo em Pânico", 1999, 100)

atlanta = Serie("Atlanta", 2018, 2)
demolidor = Serie("Demolidor", 2016, 2)

vingadores_guerra_infinita.like()
vingadores_guerra_infinita.like()
vingadores_guerra_infinita.like()
vingadores_guerra_infinita.like()
vingadores_guerra_infinita.like()

todo_mundo_em_panico.like()
todo_mundo_em_panico.like()

atlanta.like()
atlanta.like()

demolidor.like()
demolidor.like()
demolidor.like()

filmes_e_series = [vingadores_guerra_infinita, atlanta, demolidor, todo_mundo_em_panico]
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Primeiro item na playlist: {playlist_fim_de_semana[0]}')
print(f'Atlanta está na playlist? {atlanta in playlist_fim_de_semana}')
