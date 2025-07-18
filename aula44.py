"""
For + Range
range -> range(start, stop, step)
"""
# novo_numero = '' # uma variável chamada novo_numero é criada e inicializada como uma string vazia
# numeros = range(5, 10, 2) # a função range() é muito útil para gerar sequências de números, start / stop / step
# for numero in numeros: # loop for, cada iteração, a variável numero receberá o próximo valor da sequência gerada por range
#     print(numero) # dentro do loop, esta linha imprime o valor atual da variável numero
#     print(novo_numero) # também dentro do loop, esta linha imprime o valor da variável novo_numero

novo_numero = '' # uma variável chamada novo_numero é criada e inicializada como uma string vazia
numeros = range(5, 10, 2) # a função range() é muito útil para gerar sequências de números, start / stop / step
for numero in numeros: # loop for, cada iteração, a variável numero receberá o próximo valor da sequência gerada por range
    print(numero) # dentro do loop, esta linha imprime o valor atual da variável numero
    novo_numero += f'*{numero}' # constroi uma nova string, e começa com * e é seguida pelo valor de numero convertido para string
    print(novo_numero) # imprime o estado atual da string novo_numero, após a adição do asterisco e do número daquela iteração