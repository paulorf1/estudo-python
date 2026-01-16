"""
Projeto: Planejador de Treino
Descrição: Sistema em console para cadastro e gerenciamento de treinos e exercícios.
Autor: Paulo Ramos
"""

# Sistema de planejamento de treinos em console que permite cadastrar treinos, adicionar exercícios, registrar status de execução
# e listar treinos por categoria. Utiliza listas, dicionários, funções e menus interativos

from treinos import (
    listar_treinos,
    criar_treino,
    adicionar_exercicio,
    marcar_exercicio_feito,
)


def menu():
    print("=== PLANEJADOR DE TREINO ===")
    print("1 - Listar treinos")
    print("2 - Criar treino")
    print("3 - Adicionar exercício a um treino")
    print("4 - Marcar exercício como feito")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_treinos()

        elif opcao == "2":
            nome = input("Nome do treino: ")
            criar_treino(nome)

        elif opcao == "3":
            listar_treinos()
            try:
                i = int(input("Número do treino: "))
                nome = input("Nome do exercício: ")
                series = input("Séries (ex: 3x10): ")
                adicionar_exercicio(i, nome, series)
            except ValueError:
                print("\nDigite um número válido.\n")

        elif opcao == "4":
            listar_treinos()
            try:
                t = int(input("Número do treino: "))
                e = int(input("Número do exercício: "))
                marcar_exercicio_feito(t, e)
            except ValueError:
                print("\nDigite números válidos.\n")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida.\n")


if __name__ == "__main__":
    main()
