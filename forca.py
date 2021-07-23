from itertools import count


def jogar_forca():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

    pontos = 1000
    pontos_perdidos = 0

    palavra_secreta = ("banana").upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        tentativa = input ("Qual a letra? ").upper().strip()
        index = 0

        for letra in palavra_secreta:
            if (tentativa == letra):
                letras_acertadas[index] = letra;
            index = index + 1
        print(letras_acertadas)

        palavra_secreta.find(tentativa)

    print("\nFim do jogo!")
    print("Pontuação total de: {}".format((pontos)))
    print("*********************************")

if (__name__ == "__main__"):
    jogar_forca()