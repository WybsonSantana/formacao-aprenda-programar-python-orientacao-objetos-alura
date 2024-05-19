def jogar():
    print("*********************************")
    print("* Bem-vindo ao Jogo da Forca *")
    print("*********************************")

    palavra_secreta = "banana"

    acertou_palavra = False
    enforcou = False

    while not acertou_palavra and not enforcou:
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra {} na posição {}.".format(letra, index))
            index = index + 1

        print("Jogando!")

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
