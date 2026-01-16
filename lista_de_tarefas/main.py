"""
Projeto: Lista de Tarefas
Descrição: Gerenciador de tarefas em console com persistência em JSON.
Autor: Paulo Ramos
"""

# Este projeto é um gerenciador de tarefas em linha de comando, com persistência de dados em arquivo JSON.
# O objetivo é praticar conceitos fundamentais da linguagem, incluindo funções, classes, listas, manipulação de arquivos e serialização em JSON.

import json
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
