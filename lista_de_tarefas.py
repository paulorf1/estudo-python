# Este projeto é um gerenciador de tarefas em linha de comando, com persistência de dados em arquivo JSON. 
# O objetivo é praticar conceitos fundamentais da linguagem, incluindo funções, classes, listas, manipulação de arquivos e serialização em JSON.
import json


def menu():
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefa')
    print('3 - Concluir tarefa')
    print('4 - Remover tarefa')
    print('0 - Sair')


class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida


def adicionar_tarefas():
    descricao = input('Qual é a tarefa? ')
    novo_id = len(tarefas) + 1
    tarefa = Tarefa(novo_id, descricao)
    tarefas.append(tarefa)
    salvar_tarefas()
    print('Tarefa adiciona com sucesso!')


def listar_tarefas():
    if not tarefas:
        print('Nenhuma tarefa cadastrada')
    else:
        for tarefa in tarefas:
            status = 'Concluida' if tarefa.concluida else 'Pendente'
            print(f"[{tarefa.id}] {tarefa.descricao} - {status}")


def concluir_tarefa():
    id_busca = int(input('Qual é o ID da tarefa a concluir? '))
    encontrada = False

    for tarefa in tarefas:
        if tarefa.id == id_busca:
            if tarefa.concluida:
                print('Esta tarefa já está concluida')
            else:
                tarefa.concluida = True
                salvar_tarefas()
                print('Tarefa concluida com sucesso!')
                encontrada = True
            break

    if not encontrada:
        print('Tarefa não encontrada')


def remover_tarefa():
    id_busca = int(input('Digite o ID da tarefa a ser removida: '))
    removida = False

    for i in range(len(tarefas)):
        if tarefas[i].id == id_busca:
            tarefas.pop(i)
            salvar_tarefas()
            print('Tarefa removida com sucesso')
            removida = True
            break

    if not removida:
        print('Tarefa não encontrada')


def salvar_tarefas():
    lista_para_json = []
    for tarefa in tarefas:
        lista_para_json.append({
            'id': tarefa.id,
            'descricao': tarefa.descricao,
            'concluida': tarefa.concluida
        })
    with open('tarefas.json', "w") as arquivo:
        json.dump(lista_para_json, arquivo, indent=4)


def carregar_tarefas():
    global tarefas
    tarefas = []

    try:
        with open('tarefas.json', "r") as arquivo:
            lista_json = json.load(arquivo)
            for item in lista_json:
                tarefa = Tarefa(
                    item['id'],
                    item['descricao'],
                    item['concluida']
                )
                tarefas.append(tarefa)

    except (FileNotFoundError, json.JSONDecodeError):
        tarefas = []


carregar_tarefas()

while True:
    menu()
    opcao = input('Escolha uma das opções: ')
    if opcao == '1':
        adicionar_tarefas()
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        concluir_tarefa()
    elif opcao == '4':
        remover_tarefa()
    elif opcao == '0':
        break
    else:
        print('Opção inválida')
