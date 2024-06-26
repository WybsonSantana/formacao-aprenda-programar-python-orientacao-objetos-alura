from collections import defaultdict, Counter

from conta import Conta

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)

print(len(assistiram))

print(set(assistiram))

print(set([1, 2, 3, 1]))

print(type({1, 2}))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)

# print(usuarios_machine_learning[3])

for usuario in set(assistiram):
    print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning)

print(usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning

print(15 in fez_ds_mas_nao_fez_ml)

print(23 in fez_ds_mas_nao_fez_ml)

print(usuarios_data_science ^ usuarios_machine_learning)

usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

print(usuarios)

usuarios = frozenset(usuarios)
print(usuarios)

print(type(usuarios))

# usuarios.add(134)

meu_texto = 'Bem vindo meu nome é Fulano eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
print(meu_texto.split())

print(set(meu_texto.split()))

aparicoes = {
    'Fulano': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

print(type(aparicoes))

print(aparicoes['Fulano'])

print(aparicoes['cachorro'])

# print(aparicoes['xpto'])

print(aparicoes.get('xpto', 0))

print(aparicoes.get('cachorro', 0))

aparicoes = dict(Fulano=2, cachorro=1)
print(aparicoes)

aparicoes = {
    'Fulano': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

aparicoes['Beltrano'] = 1

print(aparicoes)

aparicoes['Beltrano'] = 2

print(aparicoes)

del aparicoes['Beltrano']

print(aparicoes)

print('cachorro' in aparicoes)

print('Beltrano' in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

print(1 in aparicoes.values())

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, '=', valor)

print(["palavra {}".format(chave) for chave in aparicoes.keys()])

meu_texto = 'bem vindo meu nome é Fulano eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

int()

dicionario = defaultdict(int)
dicionario['Fulano']

dicionario['Fulano'] = 15
print(dicionario['Fulano'])

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

contas = defaultdict(Conta)

contas[15]
contas[17]
contas[15]

aparicoes = Counter()

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

aparicoes = Counter(meu_texto.split())

print(aparicoes)

texto1 = """
Para começar a fazer vendas online, uma empresa que fabrica adesivos criou uma página para pré cadastro de cartão de crédito que contém campos como nome, idade, endereço, CPF entre outros.

O problema é que alguns cadastros não possuem um formato de CPF válido, isso porque o campo não possui nenhuma validação. Ou seja, o campo está aceitando não só números como letras e outros tipos de caractere.

O que vamos fazer é encontrar uma maneira de ajudar o usuário de forma mais clara possível a preencher o cadastro e garantir a validação no front-end antes que os dados sejam enviados para o back-end.

Como podemos notar não temos nenhuma validação, então fica confuso se devemos ou não colocar ponto ou traço no CPF e pode acontecer do usuário colocar outros caracteres no campo sem querer.

Para isso evitar que isso ocorra vamos usar o atributo pattern do HTML5 que nos permite fazer uso das famosas expressões regulares que nada mais são que padrões utilizados para selecionar caracteres em uma string.

Na nossa verificação vamos usar a lista [0-9], esse padrão indica que queremos os números de 0 até 9 e o intervalo {11}, indicando que temos que ter um número de 11 dígitos no nosso campo.

Com a adição do pattern nosso campo de CPF ficou da seguinte maneira:

Com a ajuda do pattern e das expressões regulares conseguimos resolver uma parte da tarefa, agora o que precisamos fazer encontrar uma maneira de formatar o CPF no padrão que precisamos enviar ao back-end.

Mais um pouco de Regex

Para começar vamos criar uma função que vai ser responsável por formatar o CPF. Dentro dessa função vamos ter as variáveis :

elementoAlvo: responsável pelo parâmetro que vai ser passado na função
cpfAtual: responsável por capturar os números do CPF digitados
cpfAtualizado: responsável por receber o CPF formatado.
"""

texto2 = """
Vamos imaginar uma empresa como o Nubank, seu nome é ByteBank. A primeira vista ela vende cartões de crédito e possui uma estratégia de marketing de conteúdo para seus clientes (Business to Consumer, B2C).

Agora ela está lançando um novo cartão focado em empresas e quer criar uma estratégia de marketing de conteúdo para outras empresas (business to business, B2B).

Como eles podem criar essa estratégia? É possível utilizar ideias e ferramentas do marketing de conteúdo B2C para o B2B?

No marketing de conteúdo criado para B2C da ByteBank é muito enfatizado que as principais vantagens da empresa são:

saber o limite na hora;
não pagar qualquer tarifa e
não ter que lidar com burocracia na hora de fazer o cartão.

Então, todo o plano é focado em criar conteúdos sobre questões relacionadas ao mundo financeiro, para mostrar que a empresa é especialista no assunto, transmitindo uma confiança aos clientes.

A equipe de marketing escreveu um texto no qual foram explicadas todas as taxas do cartão de crédito. Depois de explicar com detalhes o que é cada taxa, foi mostrado o porquê do cartão dessa empresa não cobrar nenhuma delas.

Para mostrar na prática o quanto o consumidor economizaria, eles deram como um exemplo que mostram o que pode ser comprado com o dinheiro economizado em tarifas do cartão. Veja como ficou o texto:

Se a tarifa é de 30 reais por mês, depois de um ano: 30 (tarifa) * 12 (meses) = 360, você gasta R$ 360,00 só em tarifas! Não seria muito melhor comprar um Kindle ou dois jogos para Playstation 4 ou, até mesmo, ir uma vez por mês ao cinema (e pagando inteira) com esse dinheiro em vez de pagá-lo em tarifas?

Será que se pode fazer a mesma coisa para o B2B, já que não existem tarifas para empresas também?

As empresas que querem comprar um produto precisam avaliar muito bem toda a compra, sempre se perguntando se aquele produto realmente compensa para ela, principalmente a longo prazo.

Então, e se fosse dito coisas que a empresa poderia fazer com o dinheiro que também vão trazer um retorno financeiro, ao contrário das taxas dos bancos? Como fazer pesquisas com usuários, desenvolver novos produtos, treinar pessoas para marketing, entre outras coisas?

Pensando nessas diferenças, utilizamos o mesmo exemplo: quanto seria economizado por ano pela empresa cliente. Porém, no texto inteiro, queremos também mostrar dicas de como ela pode poupar, de diversas maneiras, mesmo usando um cartão de crédito. Então, o exemplo de economia no texto ficou assim:

Pensando que a tarifa para empresas é mais barata que para pessoas físicas, ou seja, de 30 reais, passa a ser 10 reais por cartão para cada colaborador, e dez cartões serão feitos, cada um pertencendo a colaborador, depois de um ano, serão pagos: 10 (de tarifa) * 10 (quantidade de cartões) * 12 (meses do ano) = 1200.

Assim, a organização gastaria R$ 1.200,00 para manter os cartões durante esse período. Agora, se os cartões não possuem tarifa nenhuma, em vez de pagar esse valor, a empresa economizará R$1.200,00.

Agora, com essa economia, você poderia investir em treinamentos ou eventos, que, após um tempo, poderiam aumentar ainda mais o retorno da empresa.

Foi usada uma linguagem mais formal do que a B2C porque quando estamos lidando com empresas temos que ser mais práticos e mostrar exatamente o que a empresa ganha, e, no caso, até como poderia ganhar mais depois.

Além dessa mudança na linguagem, tivemos ideias diferentes de conteúdo. No B2C foram apresentados conhecimentos a respeito de cada taxa, para que a pessoa entenda o que está pagando e confie em empresas que não cobra as taxas.

Agora para B2B foram apresentadas formas para economizar no cartão, pois, muitas vezes, os empresários sabem o que é cada taxa do cartão e tem que utilizá-lo mesmo assim. Então, mostramos como ele pode economizar e, uma dessas formas, é usar o cartão da ByteBank.

Nesse mesmo texto para B2B também acrescentamos o conteúdo de outra vantagem do cartão: poder determinar um limite de gastos para cada categoria nos cartões dos funcionários da empresa.

Dessa forma, os funcionários não podem gastar mais do que o determinado e, assim, a empresa consegue economizar e planejar os gastos e não extrapolar com compras dos funcionários.

O foco da comunicação B2B que utilizamos foi dar dicas para não cometer erros e economizar mais, para que a empresa perceba que utilizar o cartão é vantagem.

E caso a sua empresa seja diferente da ByteBank, seja só B2B e não tenha nenhum plano de comunicação focado para B2C para se basear?

Existem diversas empresas B2B:

as que vendem tanto para B2B quanto para B2C, como a ByteBank;
as que vendem para ambos os consumidores, mas possuem um foco maior no B2B, como a Marmotex, que tem como serviço entrega de marmitas e entregam tanto para consumidores quanto empresas, mas possuem um foco maior em organizações e catering para eventos, ou seja, B2B
as empresas somente B2B, como as de agências de publicidade.

Cada uma das empresas que são B2B possui um produto e um serviço para mostrar.

Então, caso você trabalhe em uma empresa que não possui um plano de marketing de conteúdo para B2C para se basear, é só seguir a ideia do marketing de conteúdo, de passar informações relacionados a sua empresa, tornando-a uma autoridade no assunto. E, além disso, mostrar maneiras que o seu produto e/ou serviço pode ajudar a empresa em determinado tema.

No B2B, como no marketing de conteúdo focado no B2C, é importante frisar a importância e a relevância do produto e/ou serviço para o cliente. E, melhor, a longo prazo.

A empresa cliente precisa entender e saber que a vantagem trazida pelo produto será duradoura. Pois o processo de compra B2B é mais longo justamente porque há muito em jogo e muitas pessoas envolvidas.

Mudar de produto ou serviço é trabalhoso e pode causar prejuízo para a empresa, assim, eles buscam e precisam de garantias de que a solução funcionará por muito tempo.

Assim, como no marketing B2C, os tipos de conteúdo devem se atentar aos clientes em cada fase do funil de marketing de conteúdo para trazer o conteúdo certo para a empresa em cada momento da obtenção do cartão.

Para isso, a Bytebank utilizou dados, números, infográficos e mostrou com exemplos práticos maneiras de ajudar a contratante. Também escreveu conteúdos com histórias de empresas – os chamados cases de sucesso – que obtiveram lucro ou sucesso com o produto/serviço.

Além disso, apresentou novidades e dicas tanto da sua empresa, que passou a fornecer uma conta para pessoas físicas e jurídicas, quanto do segmento dela, com informações que podem ser úteis ao cliente do setor financeiro.

Como vimos, as principais diferenças entre os conteúdos B2C para o B2B são a linguagem, que deve ser mais formal se for B2B e apelar para o emocional se for B2C.

No B2B você estará lidando com pessoas que tomam decisões nas empresas, então deverá mostrar como o produto pode ajudar a empresa, de preferência a longo prazo.

Fora isso, o tipo de conteúdo pode ser o mesmo do marketing de conteúdo B2C. Passando desde textos sobre novidades, inovações e dicas na área, até infográficos com dados de pesquisas, vídeos, áudios de podcast, imagens e publicações nas redes sociais.

Também, para conteúdo B2B, é muito comum encontrar whitepapers, grupos de usuários, meetups, cases de sucesso, trial gratuito, e até mesmo vídeos ou campanhas e posts de marketing com influenciadores.
"""


def analisar_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisar_frequencia_de_letras(texto1)

analisar_frequencia_de_letras(texto2)
