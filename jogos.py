import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("Escolha o seu jogo!")
    print("*********************************")

    escolha = int(input("Digite 1 para Forca e 2 para Adivinhação: "));

    if (escolha == 1):
        forca.jogar_forca()
    elif (escolha == 2):
        adivinhacao.jogar_adivinhacao()
    else:
        print("Você não escolheu um jogo possível, tente novamente.")

if (__name__ == "__main__"):
    escolher_jogo()