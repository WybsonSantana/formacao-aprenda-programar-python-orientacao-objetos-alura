import requests

from acesso_cep import BuscaEndereco

cep = 25870145
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

request = requests.get('https://viacep.com.br/ws/01001000/json/')
print(request.text)

acesso = objeto_cep.acessar_via_cep()
print(acesso)
