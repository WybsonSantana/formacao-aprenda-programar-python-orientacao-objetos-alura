from conta_corrente import ContaCorrente


def faz_processamento_de_visualicacao(input_list=None):
    if input_list is None:
        input_list = list()
        print(len(input_list))
        print(input_list)
        input_list.append(17)


idades = [39, 30, 27, 18]

idades.append(15)

for idade in idades:
    print(idade)

idades.remove(30)
idades.remove(27)
idades.append(27)
print(idades)

# idades.clear()
# print(idades)

if 15 in idades:
    idades.remove(15)
    print(idades)

idades.insert(0, 20)
print(idades)

idades.extend([19, 28])
print(idades)

idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem)

idades_maiores_que_21 = [idade for idade in idades if idade > 21]
print(idades_maiores_que_21)

faz_processamento_de_visualicacao()

conta_do_fulano = ContaCorrente(15)
print(conta_do_fulano)

conta_do_fulano.deposita(500)
print(conta_do_fulano)

conta_do_beltrano = ContaCorrente(47685)
conta_do_beltrano.deposita(1000)
print(conta_do_beltrano)

contas = [conta_do_fulano, conta_do_beltrano]
for conta in contas:
  print(conta)

contas = [conta_do_fulano, conta_do_beltrano, conta_do_fulano]

print(contas[0])

conta_do_fulano.deposita(100)

print(contas[0])

print(conta_do_fulano)

print(contas[2])

contas[2].deposita(300)

print(conta_do_fulano)

def deposita_para_todas(contas):
  for conta in contas:
    conta.deposita(100)

contas = [conta_do_fulano, conta_do_beltrano]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

deposita_para_todas(contas)
print(contas[0], contas[1], contas[2])

fulano = ('Fulano', 37, 1981) # tupla
beltrano = ('Beltrano', 31, 1987)
# ciclano = (39, 'Ciclano', 1979) # ruim

fulano.append(6754)

conta_do_fulano = (15, 1000)
# conta_do_fulano.deposita() # variação OO
conta_do_fulano[1]

conta_do_fulano[1] += 100

def deposita(conta): # variação "funcional"(separando o comportamento dos dados)
  novo_saldo = conta[1] + 100
  codigo = conta[0]
  return (codigo, novo_saldo)

deposita(conta_do_fulano)

conta_do_fulano

conta_do_fulano
conta_do_fulano = deposita(conta_do_fulano)
