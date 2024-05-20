import random


def jogar():
    imprimir_mensagem_de_abertura()

    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou_palavra = False
    enforcou = False
    erros = 0
    maximo_de_tentativas = 7

    while not acertou_palavra and not enforcou:
        chute = pedir_chute_ao_jogador()

        if chute in palavra_secreta:
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Errou! Faltam {} tentativas.".format(maximo_de_tentativas - erros))
            desenhar_forca(erros)

        enforcou = erros == maximo_de_tentativas
        acertou_palavra = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou_palavra:
        imprimir_mensagem_de_vencedor()
    else:
        imprimir_mensagem_de_perdedor(palavra_secreta)


def imprimir_mensagem_de_abertura():
    print("*********************************")
    print("* Bem-vindo ao Jogo da Forca *")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    numero_da_linha = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_da_linha].upper()
    return palavra_secreta


def inicializar_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pedir_chute_ao_jogador():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marcar_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprimir_mensagem_de_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimir_mensagem_de_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
