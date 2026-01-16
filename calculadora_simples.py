"""
Projeto: Calculadora Simples
Descrição: Calculadora em console com operações básicas (soma, subtração, multiplicação e divisão),
utilizando funções e validação de entrada do usuário.
Autor: Paulo Ramos
"""

# Calculadora básica com operações matemáticas em Python.

while True: # loop infinito, a calculadora continuará pedindo entradas até que uma condição break seja satisfeita
    num_1 = input('Digite o primeiro número: ') # Pede o primeiro número ao usuário
    operador = input('Digite o operador: (+, -, *, /:) ') # Pede o operador ao usuário
    num_2 = input('Digite o segundo número: ') # Pede o segundo número ao usuário
    numeros_validos = None # esta variável atua como uma flag, para indicar se os números foram convertidos com sucesso
    operadores_permitidos = '+-/*' # string que contém todos os operadores válidos, facilitando a verificação
    num_1_float = 0 # inicializa as variáveis que armazenarão os números convertidos, boa prática para garantir que elas existam mesmo se a conversão falhar
    num_2_float = 0 # inicializa as variáveis que armazenarão os números convertidos, boa prática para garantir que elas existam mesmo se a conversão falhar
    try: 
        num_1_float = float(num_1) # tenta converter num_1 e num_2 para float
        num_2_float = float(num_2) # tenta converter num_1 e num_2 para float
        numeros_validos = True # se a conversão for bem-sucedida, numeros_validos é definido como True
    except: # se qualquer erro (ValueError seria o mais comum aqui) ocorrer durante a conversão, este bloco é executado
        numeros_validos = None # numeros_validos é explicitamente definido como None novamente
        if numeros_validos is None: # esta condição verifica se a conversão falhou
           print('Um ou ambos os números são inválidos.') # se falhou, informa ao user
           continue # esta instrução pula o restante do código na iteração atual, e imediatamente retorna ao início do loop while, pedindo novas entradas
    if operador not in operadores_permitidos: # verifica se o operador digitado não está na string operadores_permitidos
           print('Operador invalido.') # se não estiver, imprime uma mensagem de erro e usa continue para reiniciar o loop
    if len(operador) > 1: # garante que o usuário digitou apenas um caractere para o operador
           print('Digite apenas um operador.') #  se digitar mais de um, imprime erro e usa continue
           continue #  se digitar mais de um, imprime erro e usa continue
    print('Realizando sua conta, confira o resultado:') 
    if operador == '+': # se o operador for + exibe o print abaixo 
        print(f'{num_1_float}+{num_2_float} =',num_1_float + num_2_float) # se for +
    elif operador == '-': # se o operador for - exibe o print abaixo
        print(f'{num_1_float}-{num_2_float} =',num_1_float - num_2_float) # se for - 
    elif operador == '*': # se o operador for * exibe o print abaixo
        print(f'{num_1_float}*{num_2_float} =',num_1_float * num_2_float) # se for * 
    elif operador == '/': # # se o operador for / e não for 0 exibe o print abaixo
        if num_2_float == 0: # isso impede um erro de divisão por zero, imprime uma mensagem específica, e usa continue
            print('Erro: Não é possivel dividir por zero.') # mensagem de erro
            continue # reinicia o loop 
        print(f'{num_1_float}/{num_2_float} =',num_1_float / num_2_float) # se for /
    else: # é um "catch-all" que, idealmente, nunca deveria ser atingido se todas as validações anteriores estiverem corretas
        print('Não deveria chegar aqui') # mensagem de erro 
    sair = input('Quer sair? [s]im:').lower().startswith('s') # pede ao usuário se ele quer sair, .lower(): converte a entrada para minúsculas
    # .startswith('s'): verifica se a string resultante começa com a letra 's' 
    if sair is True: # se sair for True, a instrução break é executada, encerrando o loop while e finalizando o programa
     break
