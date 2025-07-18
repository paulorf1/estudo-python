"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
import re # importa o módulo re, que fornece operações com expressões regulares, são padrões poderosos para buscar e manipular strings
import sys # importa o módulo sys, que dá acesso a parâmetros e funções específicas do sistema, como sys.exit(), que será usada para encerrar o programa

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ') # esta linha solicita ao usuário que digite um CPF, sugerindo um formato padrão
cpf_enviado_usuario = re.sub(r'[^0-9]','',entrada) # parte para limpeza de dados, usa uma expressão regular para remover qualquer caractere que não seja um dígito (0-9) da string entrada, 

entrada_e_sequencial = entrada == entrada[0] * len(entrada) # esta linha verifica se a entrada original do usuário (antes da limpeza) consiste em dígitos sequenciais/repetidos ex: 1111111, que são considerados invalidos

if entrada_e_sequencial: # se a condição entrada_e_sequencial for True (ou seja, o CPF inserido era sequencial)
    print('Você enviou dados sequenciais.') # mensagem informativa é exibida ao user
    sys.exit() # programa é encerrado imediatamente

nove_digitos = cpf_enviado_usuario[:9] # são extraídos os primeiros nove dígitos do CPF, esses nove dígitos serão a base para calcular o primeiro dígito verificador
contador_regressivo_1 = 10 # começa em 10, ele será o peso para as multiplicações

for digito in nove_digitos: # é um loop for que itera sobre cada caractere (dígito, que ainda é uma string) presente em nove_digitos
    resultado_digito_1 += int(digito) * contador_regressivo_1 # dentro do loop, cada digito_1, ex:'7','4' é primeiro convertido para um número inteiro usando int(), esse número inteiro é então multiplicado pelo contador_regressivo_1 atual, o resultado é adicionado a variavel, resultado_digito_1
    contador_regressivo_1 -= 1 # após cada iteração, o contador_regressivo_1 é diminuído em 1, isso garante que o primeiro dígito seja multiplicado por 10, o segundo por 9, e assim por diante, até o nono dígito ser multiplicado por 2
digito_1 = (resultado_digito_1 * 10) % 11 # depois que o loop termina, esta linha calcula o valor provisório do primeiro dígito verificador, a soma acumulada é multiplicada por 10, O resultado é então dividido por 11, e o resto dessa divisão é o valor que nos interessa para o dígito verificador
digito_1 = digito_1 if digito_1 <= 9 else 0 # esta é uma expressão condicional (operador ternário), se o digito_1 calculado for um valor entre 0 e 9, ele permanece como está, no entanto, se o digito_1 calculado resultar em 10 ou 11, ele é transformado em 0 (regra específica do cálculo do dígito verificador do CPF)

dez_digitos = nove_digitos + str(digito_1) # para calcular o segundo dígito, precisamos dos nove primeiros dígitos mais o primeiro dígito verificador que acabamos de calcular, o digito_1 é convertido de volta para string (str()) para ser concatenado
contador_regressivo_2 = 11 # começa em 11

resultado_digito_2 = 0 # começa em 0
for digito in dez_digitos: # processo de loop, multiplicação e soma é o mesmo, mas usando dez_digitos e o contador_regressivo_2 que decrementa de 11 até 2
    resultado_digito_2 += int(digito) * contador_regressivo_2 # # dentro do loop, cada digito_1, ex:'7','4' é primeiro convertido para um número inteiro usando int(), esse número inteiro é então multiplicado pelo contador_regressivo_2 atual, o resultado é adicionado a variavel, resultado_digito_2
    contador_regressivo_2 -= 1 # que decrementa de 11 até 2
digito_2 = (resultado_digito_2 * 10) % 11 # depois que o loop termina, esta linha calcula o valor provisório do primeiro dígito verificador, a soma acumulada é multiplicada por 10, O resultado é então dividido por 11, e o resto dessa divisão é o valor que nos interessa para o dígito verificador
digito_2 = digito_2 if digito_2 <= 9 else 0 # esta é uma expressão condicional (operador ternário), se o digito_2 calculado for um valor entre 0 e 9, ele permanece como está, no entanto, se o digito_2 calculado resultar em 10 ou 11, ele é transformado em 0 (regra específica do cálculo do dígito verificador do CPF)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}' # concatena os nove_digitos originais com os dois dígitos verificadores (digito_1 e digito_2) que foram calculados, formando um CPF completo

if cpf_enviado_usuario == cpf_gerado_pelo_calculo: # se o CPF que o usuário digitou for exatamente igual ao CPF que o algoritmo de validação gerou, então o CPF é considerado válido
    print(f'{cpf_enviado_usuario} é válido') # exibe o cpf é valido para o user
else: # caso contrário, o CPF é inválido
    print('CPF inválido') # exibe cpf invalido ao user