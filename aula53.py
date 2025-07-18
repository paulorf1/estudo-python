"""
Enumerate - enumera iteráveis (índices)
"""


lista = ['Maria', 'Helena', 'Pedro'] # inicia com uma lista contendo três strings
lista.append('Rafael') # o método .append() adiciona 'Rafael' ao final da lista
lista_enumerada = enumerate(lista) # a função enumerate() recebe um iterável (como sua lista) e retorna um objeto enumerado, por si só, um iterador que produz pares (tuplas)
for tupla_enumerada in lista_enumerada: # loop for que itera sobre o objeto lista_enumerada, a cada iteração, enumerate(), 'gera' a próxima tupla (índice, valor), e essa tupla é atribuída à variável tupla_enumerada 
    print(tupla_enumerada) # dentro do loop, esta linha imprime a tupla completa gerada por enumerate()

# print(next(lista_enumerada))


""" Se jogar o enumerate direto, pode fazer qts for quiser"""
lista = ['Maria', 'Helena', 'Pedro'] # inicia com uma lista contendo três strings
lista.append('Rafael') # o método .append() adiciona 'Rafael' ao final da lista
for tupla_enumerada in enumerate(lista): # você cria um objeto enumerate, pense nele como um "ponteiro" ou "gerador" que sabe como produzir pares (índice, valor) da lista um de cada vez
    print(tupla_enumerada) # exibe a tupla_enumerada
for tupla_enumerada in enumerate(lista): # você cria um objeto enumerate, pense nele como um "ponteiro" ou "gerador" que sabe como produzir pares (índice, valor) da lista um de cada vez
    print(tupla_enumerada) # tupla_enumerada
for tupla_enumerada in enumerate(lista): # você cria um objeto enumerate, pense nele como um "ponteiro" ou "gerador" que sabe como produzir pares (índice, valor) da lista um de cada vez
    print(tupla_enumerada) # tupla_enumerada
    
"""faz uma lista, e pode começar no 19"""  

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz'] # inicia com uma lista contendo três strings
lista.append('João') # o método .append() adiciona 'João' ao final da lista
lista_enumerada = list(enumerate(lista, start=19)) # a função enumerate() recebe um iterável (sua lista) e, por padrão, gera pares (0, elemento_0), (1, elemento_1)
# no entanto, ao adicionar o argumento start=19, você instrui enumerate() a começar a contagem dos índices a partir de 19
print(lista_enumerada) # imprime a lista resultante de tuplas

"""formas de fazer a mesma coisa"""

lista = ['Maria', 'Helena', 'Luiz'] # inicia com uma lista contendo três strings
lista.append('João') # o método .append() adiciona 'João' ao final da lista

for tupla_enumerada in enumerate(lista): # como vimos, enumerate(lista) gera um iterador que produz tuplas no formato (índice, valor)
    a, b = tupla_enumerada # você está usando desempacotamento de tupla, como você sabe que tupla_enumerada sempre terá dois elementos (o índice e o valor)
    # você pode atribuí-los diretamente a duas variáveis separadas: a recebe o (índice) b recebe o (valor)
    print(a,b) # imprime os valores de a (o índice) e b (o valor) separadamente, com um espaço entre eles

"""formas de fazer a mesma coisa"""

for indice, nome in enumerate(lista):
    print(indice, nome)

"""formas de fazer a mesma coisa"""

for tupla_enumerada in enumerate(lista):
    indice, nome = tupla_enumerada
    print(indice, nome)

"""formas de fazer a mesma coisa"""

for tupla_enumerada in enumerate(lista):
    print('For da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

"""formas de fazer a mesma coisa"""

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])