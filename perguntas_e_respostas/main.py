"""
Projeto: Perguntas e Respostas
Descrição: Jogo de perguntas em console com múltiplas alternativas, validação de respostas e
pontuação final do usuário.
Autor: Paulo Ramos
"""

# Exercício em Python com perguntas e respostas para praticar condicionais e entrada de dados.

from jogo import jogar


def main():
    print("=== QUIZ ===")
    input("Pressione ENTER para começar...")
    jogar()


if __name__ == "__main__":
    main()
