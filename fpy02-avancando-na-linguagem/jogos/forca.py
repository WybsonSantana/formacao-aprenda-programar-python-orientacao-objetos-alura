import random


def jogar():
    imprimir_mensagem_de_abertura()

    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    acertou_palavra = False
    enforcou = False
    erros = 0
    maximo_de_tentativas = 6

    while not acertou_palavra and not enforcou:
        chute = pedir_chute_ao_jogador()

        if chute in palavra_secreta:
            marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Errou! Faltam {} tentativas.".format(maximo_de_tentativas - erros))

        enforcou = erros == maximo_de_tentativas
        acertou_palavra = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou_palavra:
        imprimir_mensagem_de_vencedor()
    else:
        imprimir_mensagem_de_perdedor()


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
    print("Você ganhou!")


def imprimir_mensagem_de_perdedor():
    print("Você perdeu!")


if __name__ == "__main__":
    jogar()
