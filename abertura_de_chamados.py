def mostrar_menu():
    print('1 - Abrir chamado')
    print('2 - Listar chamados')
    print('3 - Encerrar chamados')
    print('4 - Sair')


chamados = []


def abrir_chamado():
    titulo = input('Titulo do chamado:')
    novo_id = len(chamados) + 1
    chamado = {
        'id': novo_id,
        'titulo': titulo,
        'status': 'Aberto'
    }
    chamados.append(chamado)
    print('Chamado aberto com sucesso!')


def listar_chamados():
    if not chamados:
        print('Nenhum chamado cadastrado')
    else:
        for chamado in chamados:
            print(chamado)


def encerrar_chamado():
    id_busca = input('Digite o ID do chamado: ')
    id_busca = int(id_busca)

    encontrado = False

    for chamado in chamados:
        if chamado['id'] == id_busca:
            chamado['status'] = 'Encerrado'
            encontrado = True
            print('Chamado encerrado com sucesso!')
            break
    if not encontrado:
        print('Chamado não encontrado')


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        abrir_chamado()
    elif opcao == '2':
        listar_chamados()
    elif opcao == '3':
        encerrar_chamado()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
