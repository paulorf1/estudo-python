# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ') #pede ao usuário para digitar um nome e armazena como uma string na variável nome
encontrar = input('Digite o que deseja encontrar: ') #pede ao usuário para digitar o que deseja encontrar, e é armazenado em encontrar

if encontrar in nome: #o operador in verifica se a string 'encontrar' existe como uma substring dentro da string à direita 'nome'
    print(f'{encontrar} está em {nome}') #se a string 'encontrar' for encontrada dentro de 'nome', a condição é avaliada como True, e exibe esse print
else:
    print(f'{encontrar} não está em {nome}') #se a string 'encontrar' não foi encontrada dentro de 'nome', exibe esse print