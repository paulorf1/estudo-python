from tarefas import listar_tarefas, adicionar_tarefa, remover_tarefa


def menu():
    print("=== LISTA DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()

        elif opcao == "2":
            descricao = input("Digite a tarefa: ")
            adicionar_tarefa(descricao)

        elif opcao == "3":
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa: "))
                remover_tarefa(indice)
            except ValueError:
                print("\nDigite um número válido.\n")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida.\n")


if __name__ == "__main__":
    main()
