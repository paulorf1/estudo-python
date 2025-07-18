"""
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """

entrada = input ('Digite um número:') # pede ao user digitar um numero, e salvo como string
if entrada.isdigit(): # o método .isdigit() de strings, retorna True se todos os caracteres na string forem dígitos (0-9) e a string não for vazia, (ele não aceita numeros negativos nem decimais)
    entrada_int = int(entrada) # se entrada.isdigit() for True, o user digitou numero inteiro positivo, programa o transforma para int e segue o if
    par_impar = entrada_int % 2 == 0 # o operador % (módulo ou resto da divisão) retorna o resto de uma divisão
    par_impar_texto = 'ímpar' # inicializa uma variável par_impar_texto com a string 'ímpar', isso serve como um valor padrão

    if par_impar: # se par_impar for True (significa que o número é par), então a linha par_impar_texto = 'par' é executada, sobrescrevendo o valor padrão
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}') # o programa imprime uma mensagem formatada (usando f-string) mostrando o número digitado e se ele é 'par' ou 'ímpar'
else:
    print('Você não digitou um número inteiro') # se entrada_int.isdigit()for False, pula para esse Else e imprime esse print

# outra forma de fazer
entrada = input ('Digite um número:') #pede ao user digitar um numero, e salvo como string
try: # como um 'bloco de testes', você coloca aqui o código que pode falhar, se tudo correr bem, o Python executa todo o try e ignora o except
    entrada_int = float(entrada) # aqui você tenta converter a entrada (str) para um numero (float), se der errado vai para o except, se der certo segue
    par_impar = entrada_int % 2 == 0 # o operador % (módulo ou resto da divisão) retorna o resto de uma divisão
    par_impar_texto = 'ímpar' # variavel de texto é inicializada como 'impar'

    if par_impar: # se a variavel par_impar for True, o numero é par, par_impar_texto é atualizada para 'par'
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}') # imprimi o numero e sua clasificação
except:
    print('Você não digitou um número inteiro') # se a conversão para float falhou, (é por que estava vazio, ou não era um numero), esse print é exibido

# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """

entrada = input('Digite a hora em números inteiros:') # pede para o user digitar a hora em numeros insteiros 
try: # usado para 'tentar' executar um pedaço do código que pode causar um erro, se o erro acontecer dentro do try, pula para o except
    hora = int(entrada) # programa tenta converter a entrada (string) para numero inteiro (int)
    if hora >= 0 and hora <= 11: # se a hora estiver no intervalo de 0 a 11 (inclusive), ele imprime "Bom dia".
        print('Bom dia') 
    elif hora >= 12 and hora <= 17: # se a condição anterior for falsa, e a hora estiver no intervalo de 12 a 17 (inclusive), ele imprime "Boa tarde"
        print('Boa tarde')
    elif hora >= 18 and hora <= 23: # se as condições anteriores forem falsas, e a hora estiver no intervalo de 18 a 23 (inclusive), ele imprime "Boa noite"
        print('Boa noite')
    else:
        print('Não conheço essa hora') # se nenhuma das condições if ou elif anteriores for verdadeira, significa que a hora digitada está fora do intervalo válido (0 a 23)
except:
    print('Por favor, digite apenas números inteiros') # este bloco é executado apenas se um erro ocorreu dentro do try (principalmente na tentativa de converter a string para inteiro)

# # """
# # Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# # menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# # "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# # """"

nome = input('Digita seu nome:') # pede ao user digitar seu nome e armazena em nome
tamanho_nome = len(nome) # a função len() é usada para contar o número de caracteres na string nome

if tamanho_nome >= 1: # verifica se o tamanho_nome é maior ou igual a 1, se tamanho_nome for 0 (string vazia) False, o programa pula para o else final
    if tamanho_nome <= 4: # se o nome tem 1,2,3 ou 4, a condição é True, imprime o print a seguir
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6: # se a condição anterior for False, ele verifica se o nome tem 5 ou 6 caracteres, condição sendo True...
        print('Seu nome é normal') # imprime esse print
    else: # se o nome tem mais de 6 caracteres, ele executa o print seguinte 
        print('Seu nome é muito grande') 
else: # é executado apenas se o user não digitar nada
    print('Digite mais de uma letra') # exibe esse print