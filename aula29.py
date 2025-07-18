"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('vou dobrar o numero que você digitar: ') # solicita ao usuario digitar uma numero que ficara salvo como string

try: # onde você coloca o código que pode causar um erro, "exceção", conversão da string para um número
    numero_float = float(numero_str) # tenta converter a numero_str 'que é texto' para um número de ponto flutuante 'float', se o user digitar um numero, o codigo continua
    print('STR:', numero_str) # imprime a string original
    print('FLOAT:', numero_float) # imprime a string convertida para float
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') # Calcula o dobro do numero_float e o imprime, formatando-o para duas casas decimais
except:
      print('Isso não é um número') # se a conversão falhar 'ou seja, o user digitou algo que não pode ser convertido para número, como 'abc'
      # ou apenas pressionou enter, o Python detecta um erro (ValueError) e vem para o bloco except 