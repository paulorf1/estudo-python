"""
Exercício
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Pedro'] # começa uma lista contendo 3 nomes
lista.append('Rafael') # o método .append() adiciona 'Rafael' ao final da lista

indices = range(len(lista)) # a lista agora tem 4 elementos, então len(lista) retorna 4, sem seguida range(4) é chamado, a função range() quando recebe apenas um argumento (stop),
# gera uma sequência de números inteiros que começa em 0 e vai até stop - 1, então range(4) gera a sequência 0, 1, 2, 3

for indice in indices: # esse loop for, itera sobre cada número na sequência indices (que é 0, 1, 2, 3)
    print(indice, lista[indice]) # dentro do loop, indice: imprime o número do índice atual, lista[indice]: acessa o elemento da lista que está na posição correspondente ao indice atual


""""""

lista = ['Maria', 'Helena', 'Luiz'] # começa uma lista contendo 3 nomes
indices = range(len(lista)) # len(lista) é avaliado lista tem 3 elementos, range(3) é chamado, a função range() com um único argumento (stop) gera uma sequência de números
# inteiros que começa em 0 e vai até stop - 1, assim, range(3) gera a sequência 0, 1, 2 


for indice in indices: # loop for, ele vai iterar sobre cada número na sequência que indices representa (0, 1, e 2)
    print(indice, lista[indice], type(lista[indice])) # dentro do loop, esta linha é executada para cada valor de indice, indice: Imprime o valor numérico do índice atual (ex: 0, 1, 2)
# lista[indice]: acessa o elemento da lista na posição especificada pelo indice atual (ex: lista[0] é 'Maria'), type(lista[indice]): A função type() retorna o tipo de dado do objeto que lhe é passado
# como todos os elementos da lista são strings, type(lista[indice]) retornará <class 'str'>