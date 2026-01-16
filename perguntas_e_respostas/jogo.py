from dados import PERGUNTAS


def jogar():
    pontos = 0

    for p in PERGUNTAS:
        print("\n" + p["pergunta"])
        for i, opcao in enumerate(p["opcoes"], start=1):
            print(f"{i} - {opcao}")

        try:
            resp = int(input("Resposta: "))
            if resp == p["resposta"]:
                print("Correto!")
                pontos += 1
            else:
                print("Errado!")
        except ValueError:
            print("Entrada inválida.")

    print(f"\nPontuação final: {pontos}/{len(PERGUNTAS)}\n")
