from acesso_cep import BuscaEndereco

cep = '01001000'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, uf = objeto_cep.acessar_via_cep()

print(f'Bairro: {bairro}, Cidade: {cidade}, UF: {uf}')
