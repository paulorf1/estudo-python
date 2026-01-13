# Lista de compras interativa para praticar listas e menus.

import os # importa o modulo OS, permite interagir com o sistema operacional

lista = [] # criação da variavel lista [] vazia
while True: # looping infinito, só é interrompido manualmente
    print('Selecione uma opção') # opções para o user
    opcao = input('[i]nserir [a]pagar [l]istar: ') # verifica a opção selecionada

    if opcao == 'i': # se user digitou i, executa este bloco
        os.system('cls') # limpa o terminal
        valor = input('Valor: ') # pede ao user digitar o valor a ser adicionado
        lista.append(valor) # metodo para adicionar item a 'lista'
   
    elif opcao == 'a': # se opção igual a i faça...
        indice_str = input('Escolha o indice para apagar: ') # pede o valor do 'indice' ao user, que é a posição do item na lista
        try: # usado para lidar com possiveis erros que podem acontecer
            indice = int(indice_str) # a função 'input()' sempre retorna uma string, por isso converter para int para usar como indice da lista
            del lista[indice] # comando del remove o item da lista na posição 'indice'
        except ValueError: #trata esse erro junto ao try
            print('Por favor digite número inteiro') # mensagem para o erro
        except IndexError: # trata esse erro junto ao try
            print('Índice não existe na lista') # mensagem para o erro  
        except Exception: # trata esse erro junto ao try
            print('Erro desconhecido') # mensagem para o erro 
    elif opcao == 'l': # se o user digitar l, executa esse bloco
        os.system('cls') # limpa terminal

        if len(lista) == 0: # retorna o numero de itens na lista, e se for '0', uma mensagem é exibida
            print('Nada para listar') # se não tiver nada na lista mostrar mensagem

        for i, valor in enumerate(lista): # looping, a função 'enumerate()' percorre a lista e fornece: qtd e o valor da variavel 'valor'
            print(i, valor) #mostrar enumerado
    else: # se nenhuma das opções: i,a e l forem digitadas 
        print('Por favor, escolha i, a ou l.') # mensagem para user
