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
