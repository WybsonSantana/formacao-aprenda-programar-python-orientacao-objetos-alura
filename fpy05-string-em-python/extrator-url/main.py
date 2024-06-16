from extrator_url import ExtratorURL

MOEDAS = {
    'real': {'dolar': lambda valor, cambio: valor / cambio},
    'dolar': {'real': lambda valor, cambio: valor * cambio}
}

SIMBOLOS_MOEDAS = {
    'real': 'R$',
    'dolar': 'US$'
}


def obter_parametros_de_moeda(url):
    moeda_origem = url.get_valor_parametro('moedaOrigem').lower()
    moeda_destino = url.get_valor_parametro('moedaDestino').lower()
    valor_quantidade = float(url.get_valor_parametro('quantidade'))
    return moeda_origem, moeda_destino, valor_quantidade


def converter_moeda(url, cambio):
    moeda_origem, moeda_destino, valor_quantidade = obter_parametros_de_moeda(url)

    try:
        valor_convertido = MOEDAS[moeda_origem][moeda_destino](valor_quantidade, cambio)
        simbolo_moeda = SIMBOLOS_MOEDAS[moeda_destino]
        return simbolo_moeda, valor_convertido
    except KeyError:
        raise ValueError('Não foi possível realizar a conversão!')


def main():
    url = 'https://bytebank.com/cambio?moedaOrigem=dolar&moedaDestino=real&quantidade=100'
    extrator_url = ExtratorURL(url)

    valor_dolar = 5.5

    simbolo_moeda, valor_convertido = converter_moeda(extrator_url, valor_dolar)
    print(f'Valor convertido: {simbolo_moeda} {valor_convertido:.2f}')


main()
