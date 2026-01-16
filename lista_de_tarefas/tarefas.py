from storage import carregar_tarefas, salvar_tarefas


def listar_tarefas():
    tarefas = carregar_tarefas()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\n=== TAREFAS ===")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
    print()


def adicionar_tarefa(descricao):
    tarefas = carregar_tarefas()
    tarefas.append(descricao)
    salvar_tarefas(tarefas)
    print("\nTarefa adicionada com sucesso!\n")


def remover_tarefa(indice):
    tarefas = carregar_tarefas()

    if indice < 1 or indice > len(tarefas):
        print("\nÍndice inválido.\n")
        return

    tarefa_removida = tarefas.pop(indice - 1)
    salvar_tarefas(tarefas)
    print(f"\nTarefa removida: {tarefa_removida}\n")
