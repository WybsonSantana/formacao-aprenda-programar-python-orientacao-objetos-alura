import re

padrao = '[0-9][a-z]{2}[0-9]'
texto = '123 1ac2 1cc aa1'
resposta = re.search(padrao, texto)

print(resposta.group())

padrao = '\\w{5,50}@[a-z]{3,10}.com.br'
texto = 'aaabbbcc rodrigo123@gmail.com.br'
resposta = re.search(padrao, texto)

print(resposta.group())
