#url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
url = ''

# Sanitização da URL
url = url.strip()
print(url)

# Validação da URL
if url == '':
    raise ValueError('A URL está vazia.')

# Separação da base e parâmetros
indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

# Realiza a busca por um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
valor = url_parametros[indice_valor:] if indice_e_comercial == -1 else url_parametros[indice_valor:indice_e_comercial]

print(valor)
