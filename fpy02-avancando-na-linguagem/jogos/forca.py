def jogar():
    print("*********************************")
    print("* Bem-vindo ao Jogo da Forca *")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    acertou_palavra = False
    enforcou = False

    while not acertou_palavra and not enforcou:
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim do jogo!")


if __name__ == "__main__":
    jogar()
