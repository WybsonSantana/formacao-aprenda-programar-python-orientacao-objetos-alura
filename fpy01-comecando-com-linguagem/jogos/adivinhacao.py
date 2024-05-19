print("*********************************")
print("* Bem-vindo ao Jogo de Adivinhação *")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)

chute = int(chute_str)

acertou_chute = numero_secreto == chute
chute_maior_que_numero_secreto = chute > numero_secreto
chute_menor_que_numero_secreto = chute < numero_secreto

if acertou_chute:
    print("Você acertou!")
else:
    if chute_maior_que_numero_secreto:
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif chute_menor_que_numero_secreto:
        print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo!")
