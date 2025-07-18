""""""
nome = 'Paulo Ramos Filho' #a variável nome armazena uma string com o nome da pessoa
altura = 1.71 #a variável altura armazena um número de ponto flutuante (float)
peso = 71 #a variável peso armazena um número inteiro (int)
imc = peso / (altura * altura) #é calculado a altura** 2), e o peso é dividido por esse resultado, o imc resultante será um float

linha_1 = f'{nome} tem {altura:.2f} de altura,'#esta linha cria uma string para a primeira parte da sua mensagem, com formatação
linha_2 = f'pesa {peso} quilos e seu imc é' #esta linha cria a segunda parte da mensagem, com formatação
linha_3 = f'{imc:.2f}' #esta linha cria a terceira parte da mensagem, focada no valor do IMC, com formatação

print(linha_1)#exibe o conteúdo da linha_1
print(linha_2)#exibe o conteúdo da linha_2
print(linha_3)#exibe o conteúdo da linha_3