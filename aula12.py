""""""
# nome = 'Paulo Ramos Filho' #a variável nome armazena uma string com o nome completo
# altura = 1.71 #a variável altura armazena um número de ponto flutuante (float) que representa a altura em metros
# peso = 71 #a variável peso armazena um número inteiro (int) que representa o peso em quilos
# imc = peso / (altura * altura) #formula do imc, 71 / (2.9241), o resultado dessa divisão (que será um float, pois a divisão com / sempre resulta em float)
# #é armazenado na variável imc
# print(nome, 'tem', altura, 'de altura') #imprimi os valores das variaveis, nome e altura
# print('pesa', peso, 'quilos e seu imc é', imc) #imprimi os valores das variaveis peso e imc


#exemplo de programa
nome = input('Digite seu nome: ') #pede ao usuário para digitar o nome, e salva na variavel nome
peso_str = input('Digite seu peso: ') # substitui a vírgula por ponto antes de converter para float
peso = float(peso_str.replace(',', '.'))  #float() converte a string para um número decimal (ponto flutuante), permitindo valores como 70.5
altura_str = input('Digite sua altura: ')
altura = float(altura_str.replace(',', '.'))  #float() converte a string para um número decimal (ponto flutuante), permitindo valores como 1.75
imc = peso / (altura ** 2) #divide o peso pelo resultado da altura ao quadrado, resultado float() e salvo na variavel imc
imc_arredondado = round(imc, 2) #a função round(), é usada para arredondar o valor do imc
if imc_arredondado <= 18.5: #condição: Se o valor de imc_arredondado for menor ou igual a 18.5
    print('Seu IMC está abaixo do peso') #imprimi
elif imc_arredondado >=18.5 and imc_arredondado <= 24.99: #condição: Se a condição anterior foi falsa, ele verifica esta, maior ou igual a 18.5 E menor ou igual a 24.99
    print('Seu IMC está normal') #imprimi
elif imc_arredondado >=25 and imc_arredondado <= 29.99: #condição: Se as condições anteriores forem falsas, ele verifica esta, O IMC precisa ser maior ou igual a 25 E menor ou igual a 29.99
    print('Seu IMC está sobre peso') #imprimi
else: #condição: Se nenhuma das condições if ou elif acima for verdadeira, isso significa que o imc_arredondado é maior que 29.99
    print('Seu IMC está Obeso')
print(nome, 'Você tem', altura,'m', 'de altura') #imprimi os valores das variaveis, nome e altura
print('Pesa', peso, 'quilos e seu IMC é:', imc_arredondado) #imprimi os valores das variaveis peso e imc_arredondado