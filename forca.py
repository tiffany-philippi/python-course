def jogar_forca():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    pontos = 1000
    pontos_perdidos = 0
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    while (not enforcou and not acertou):
        tentativa = input ("Qual a letra? ")
        index = 0
        for letra in palavra_secreta:
            if (tentativa == letra):
                index = index + 1
                print(tentativa)

        palavra_secreta.find(tentativa)

    print("\nFim do jogo!")
    print("Pontuação total de: {}".format((pontos)))
    print("*********************************")

if (__name__ == "__main__"):
    jogar_forca()