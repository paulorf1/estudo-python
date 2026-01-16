import random
from palavras import PALAVRAS


def jogar():
    palavra = random.choice(PALAVRAS)
    letras_descobertas = set()
    tentativas = 6

    while tentativas > 0:
        exibicao = ""
        for letra in palavra:
            if letra in letras_descobertas:
                exibicao += letra
            else:
                exibicao += "_"

        print("\nPalavra:", exibicao)
        print("Tentativas restantes:", tentativas)

        if "_" not in exibicao:
            print("\nVocê venceu!")
            return

        palpite = input("Digite uma letra: ").lower()

        if palpite in palavra:
            letras_descobertas.add(palpite)
        else:
            tentativas -= 1

    print("\nVocê perdeu! A palavra era:", palavra)
