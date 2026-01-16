def menu():
    print('1 - Criar treino')
    print('2 - Listar treino')
    print('3 - Adicionar exercício ao treino')
    print('4 - Registrar treino realizado')
    print('0 - Sair')


treinos = []


def criar_treino():
    nome = input('Nome do treino (ex: A, B, Peito, Costa): ')
    id_treino = len(treinos) + 1

    treino = {
        'id': id_treino,
        'nome': nome,
        'exercicios': [],
        'realizado': False
    }
    treinos.append(treino)
    print('Treino criado com sucesso!')

    pass


def listar_treinos():
    if not treinos:
        print('Nenhum treino cadastrado.')
    else:
        for treino in treinos:
            status = 'Realizado' if treino['realizado'] else 'Não realizado'
            print(f"[{treino['id']}] Treino {treino['nome']} - {status}")

            if not treino['exercicios']:
                print('   Sem exercícios cadastrados.')
            else:
                for exercicio in treino['exercicios']:
                    print(
                        f"   - {exercicio['nome']} | {exercicio['series']}x{exercicio['repeticoes']}")


def adicionar_exercicio():
    if not treinos:
        print('Nenhum treino cadastrado.')
        return

    listar_treinos()
    entrada = input('Digite o ID do treino: ')

    try:
        id_treino = int(entrada)
    except ValueError:
        print('Por favor, digite um número para o ID.')
        return

    treino_encontrado = None

    for treino in treinos:
        if treino['id'] == id_treino:
            treino_encontrado = treino
            break

    if treino_encontrado is None:
        print('Treino não encontrado.')
        return

    nome = input('Nome do exercício: ')
    series = input('Número de séries: ')
    repeticoes = input('Repetições: ')

    exercicio = {
        'nome': nome,
        'series': series,
        'repeticoes': repeticoes
    }

    treino_encontrado['exercicios'].append(exercicio)
    print('Exercício adicionado ao treino com sucesso! ')


def registrar_treino():
    if not treinos:
        print('Nenhum treino cadastrado.')
        return
    listar_treinos()
    id_treino = int(input('Digite o ID do treino realizado: '))
    for treino in treinos:
        if treino['id'] == id_treino:
            treino['realizado'] = True
            print('Treino registrado como realizado.')
            return
        print('Treino não encontrado.')


while True:
    menu()
    opcao = input('Escolha uma das opções: ')
    if opcao == '1':
        criar_treino()
    elif opcao == '2':
        listar_treinos()
    elif opcao == '3':
        adicionar_exercicio()
    elif opcao == '4':
        registrar_treino()
    elif opcao == '0':
        break
    else:
        print('Opção invalida!')
