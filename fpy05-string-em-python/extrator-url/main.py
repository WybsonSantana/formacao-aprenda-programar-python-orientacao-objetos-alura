from extrator_url import ExtratorURL

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
#url = None

extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print(extrator_url)
print(f'Tamanho da URL: {len(extrator_url)} caractéres')

valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)

print(extrator_url == extrator_url_2)
