import random

def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101))
    pontos = 1000
    pontos_perdidos = 0
    nivel = input("Digite o nível de dificuldade desejado: F (Fácil), M (Médio) e D (Difícil): ")
    nivel = nivel.capitalize()
    possibilidades = 0

    if (nivel == 'F'):
        possibilidades = 15
    elif (nivel == 'M'):
        possibilidades = 7
    elif (nivel == 'D'):
        possibilidades = 3
    else:
        print("Você não escolheu um nível possível, tente novamente.")

    for rodada in range(1, possibilidades + 1):
        print("Rodada: {} de {}".format(rodada, possibilidades))
        tentativa = input("Digite o seu número de 1 a 100: ")
        print("Você digitou", tentativa)
        tentativa = int(tentativa)

        if (tentativa < 1 or tentativa > 100):
            print("Você deve digitar um número de 1 a 100")
            continue

        menor = tentativa < numero_secreto
        maior = tentativa > numero_secreto
        acertou = numero_secreto == tentativa

        if acertou:
            print("Você acertou!!!!!")
            break
        else:
            if (rodada != possibilidades):
                pontos_perdidos = abs(numero_secreto - tentativa)
                pontos = pontos - pontos_perdidos

                if menor:
                    print("Tente um número maior")
                elif maior:
                    print("Tente um número menor")
            else:
                print("Você errou =(", end="\n")

        rodada = rodada + 1

    print("\nFim do jogo!")
    print("Pontuação total de: {}".format((pontos)))
    print("*********************************")

if (__name__ == "__main__"):
    jogar_adivinhacao()