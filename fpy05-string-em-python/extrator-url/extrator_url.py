import re


class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitizar_url(url)
        self.validar_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_parametros() + '\n' + 'URL Base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    def sanitizar_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def validar_url(self):
        padrao_da_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_da_url.match(self.url)

        if not match:
            raise ValueError('A URL não é válida.')

        print('A URL é válida.')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        valor = self.get_url_parametros()[indice_valor:] if indice_e_comercial == -1 else self.get_url_parametros()[
                                                                                          indice_valor:indice_e_comercial]
        return valor
