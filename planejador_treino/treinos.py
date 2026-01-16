from storage import carregar_treinos, salvar_treinos


def listar_treinos():
    treinos = carregar_treinos()

    if not treinos:
        print("\nNenhum treino cadastrado.\n")
        return

    print("\n=== TREINOS ===")
    for i, treino in enumerate(treinos, start=1):
        print(f"{i}. {treino['nome']}")

        if treino["exercicios"]:
            for ex in treino["exercicios"]:
                status = "✔" if ex["feito"] else "✖"
                print(f"   - {ex['nome']} | {ex['series']} | {status}")
        else:
            print("   (Sem exercícios)")
    print()


def criar_treino(nome):
    treinos = carregar_treinos()
    treinos.append({"nome": nome, "exercicios": []})
    salvar_treinos(treinos)
    print("\nTreino criado com sucesso!\n")


def adicionar_exercicio(indice_treino, nome, series):
    treinos = carregar_treinos()

    if indice_treino < 1 or indice_treino > len(treinos):
        print("\nTreino inválido.\n")
        return

    exercicio = {"nome": nome, "series": series, "feito": False}
    treinos[indice_treino - 1]["exercicios"].append(exercicio)
    salvar_treinos(treinos)
    print("\nExercício adicionado!\n")


def marcar_exercicio_feito(indice_treino, indice_exercicio):
    treinos = carregar_treinos()

    if indice_treino < 1 or indice_treino > len(treinos):
        print("\nTreino inválido.\n")
        return

    exercicios = treinos[indice_treino - 1]["exercicios"]

    if indice_exercicio < 1 or indice_exercicio > len(exercicios):
        print("\nExercício inválido.\n")
        return

    exercicios[indice_exercicio - 1]["feito"] = True
    salvar_treinos(treinos)
    print("\nExercício marcado como realizado!\n")
