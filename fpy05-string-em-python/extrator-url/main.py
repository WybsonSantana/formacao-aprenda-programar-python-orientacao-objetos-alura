from extrator_url import ExtratorURL

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
#url = None

extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)
