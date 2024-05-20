def jogar():
    print("*********************************")
    print("* Bem-vindo ao Jogo da Forca *")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    acertou_palavra = False
    enforcou = False
    erros = 0
    maximo_de_tentativas = 6

    print(letras_acertadas)

    while not acertou_palavra and not enforcou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Errou! Faltam {} tentativas.".format(maximo_de_tentativas - erros))

        enforcou = erros == maximo_de_tentativas
        acertou_palavra = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou_palavra:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
