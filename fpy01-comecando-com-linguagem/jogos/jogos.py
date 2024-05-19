import forca
import adivinhacao

print("*********************************")
print("******* Escolha o seu Jogo! *******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo_escolhido = int(input("Qual jogo deseja começar? "))

if jogo_escolhido == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogo_escolhido == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
