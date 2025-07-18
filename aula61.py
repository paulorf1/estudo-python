"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = '74682489070' # uma string que se chama cpf, é criada com um número de CPF de exemplo
nove_digitos = cpf[: 9] # esta linha extrai os primeiros nove dígitos da string cpf, [:9] pega os caracteres do índice 0 até o índice 8
contador_regressivo_1 = 10 # inicializa-se uma variável contador_regressivo_1 com o valor 10, este contador será usado para multiplicar cada dígito do nove_digitos em uma sequência decrescente
resultado_digito_1 = 0 # uma variável para armazenar a soma dos produtos das multiplicações é inicializada com zero

for digito_1 in nove_digitos: # é um loop for que itera sobre cada caractere (dígito, que ainda é uma string) presente em nove_digitos
    resultado_digito_1 += int(digito_1) * contador_regressivo_1 # dentro do loop, cada digito_1, ex:'7','4' é primeiro convertido para um número inteiro usando int(), esse número inteiro é então multiplicado pelo contador_regressivo_1 atual, o resultado é adicionado a variavel, resultado_digito_1
    contador_regressivo_1 -= 1 # após cada iteração, o contador_regressivo_1 é diminuído em 1, isso garante que o primeiro dígito seja multiplicado por 10, o segundo por 9, e assim por diante, até o nono dígito ser multiplicado por 2
digito_1 = ((resultado_digito_1 * 10) % 11) # depois que o loop termina, esta linha calcula o valor provisório do primeiro dígito verificador, a soma acumulada é multiplicada por 10, O resultado é então dividido por 11, e o resto dessa divisão é o valor que nos interessa para o dígito verificador
digito_1 = digito_1 if digito_1 <= 9 else 0 # esta é uma expressão condicional (operador ternário), se o digito_1 calculado for um valor entre 0 e 9, ele permanece como está, no entanto, se o digito_1 calculado resultar em 10 ou 11, ele é transformado em 0 (regra específica do cálculo do dígito verificador do CPF)
print(digito_1) # o valor do primeiro dígito verificador calculado é exibido na tela