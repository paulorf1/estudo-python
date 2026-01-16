from chamados import listar_chamados, abrir_chamado, fechar_chamado


def menu():
    print("=== SISTEMA DE CHAMADOS ===")
    print("1 - Listar chamados")
    print("2 - Abrir chamado")
    print("3 - Fechar chamado")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_chamados()

        elif opcao == "2":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            abrir_chamado(titulo, descricao)

        elif opcao == "3":
            listar_chamados()
            try:
                i = int(input("Número do chamado: "))
                fechar_chamado(i)
            except ValueError:
                print("\nDigite um número válido.\n")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida.\n")


if __name__ == "__main__":
    main()
