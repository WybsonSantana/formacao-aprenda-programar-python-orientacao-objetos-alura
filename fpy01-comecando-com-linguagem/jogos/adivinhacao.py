import random


def jogar():
    print("*********************************")
    print("* Bem-vindo ao Jogo de Adivinhação *")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_pontos = 1000
    total_de_tentativas = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel_de_dificuldade = int(input("Defina o nível: "))

    if nivel_de_dificuldade == 1:
        total_de_tentativas = 20
    elif nivel_de_dificuldade == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}.".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)

        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou_chute = numero_secreto == chute
        chute_maior_que_numero_secreto = chute > numero_secreto
        chute_menor_que_numero_secreto = chute < numero_secreto

        if acertou_chute:
            print("Você acertou! Você fez {} pontos.".format(total_de_pontos))
            break
        else:
            if chute_maior_que_numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif chute_menor_que_numero_secreto:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            total_de_pontos = total_de_pontos - pontos_perdidos

    print("Fim do jogo!")
