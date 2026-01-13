# Inversão de texto para praticar manipulação de strings.

nome = input('Digite o seu nome:') #pede ao usuário para digitar o nome, e armazena na variavel nome
idade = input('Digite a sua idade:') #pede ao usuário para digitar a idade, e armazena na variavel idade
if nome and idade: # o and verifica se ambas as variaveis contem algum valor (não são vazias), se tiverem valor executa o codigo dentro do if
    print(f'Seu nome é: {nome}') # exibe o nome
    print(f'Seu nome invertido é: {nome[::-1]}') # exibe o nome invertido
    if ' ' in nome:  # usa o operador in para verificar se a string nome contém um espaço (' ')
        print(f'Seu nome contém espaços') # se houver espaço executa esse print
    else: 
        print(f'Seu nome não contém espaços') # se não houver espaço executa esse print

    print(f'Seu nome tem {len(nome)} letras') # a função len(), retorna o número de caracteres, inclui espaços se houver 
    print(f'A primeira letra do seu nome é {nome[0]}') # o indice [0], referece ao primeiro caractere de uma string, exibindo a primeira letra da variavel nome 
    print(f'A última letra do seu nome é {nome[-1]}') # # o indice [-1], referece ao ultimo caractere de uma string, exibindo a ultima letra da variavel nome 
else:
    print("Desculpe, você deixou campos vazios") # se nome e idade forem vazios, esse print sera executado
nome = input('Digite o seu nome:') #pede ao usuário para digitar o nome, e armazena na variavel nome
idade = input('Digite a sua idade:') #pede ao usuário para digitar a idade, e armazena na variavel idade
if nome and idade: # o and verifica se ambas as variaveis contem algum valor (não são vazias), se tiverem valor executa o codigo dentro do if
    print(f'Seu nome é: {nome}') # exibe o nome
    print(f'Seu nome invertido é: {nome[::-1]}') # exibe o nome invertido
    if ' ' in nome:  # usa o operador in para verificar se a string nome contém um espaço (' ')
        print(f'Seu nome contém espaços') # se houver espaço executa esse print
    else: 
        print(f'Seu nome não contém espaços') # se não houver espaço executa esse print

    print(f'Seu nome tem {len(nome)} letras') # a função len(), retorna o número de caracteres, inclui espaços se houver 
    print(f'A primeira letra do seu nome é {nome[0]}') # o indice [0], referece ao primeiro caractere de uma string, exibindo a primeira letra da variavel nome 
    print(f'A última letra do seu nome é {nome[-1]}') # # o indice [-1], referece ao ultimo caractere de uma string, exibindo a ultima letra da variavel nome 
else:
    print("Desculpe, você deixou campos vazios") # se nome e idade forem vazios, esse print sera executado
