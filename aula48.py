"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# #        +01234
# #        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# # print(bool([]))  # falsy
# # print(lista, type(lista))

# #        0    1      2              3    4
# #       -5   -4     -3             -2   -1
# lista = [123, True, 'Luiz Otávio',  1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

# #        0   1   2   3   4   5
lista = [10, 20, 30, 40] # lista inicializada com quatro elementos
# lista[2] = 300 
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # O método .append() adiciona um elemento ao final da lista
lista.pop() # O método .pop() remove e retorna o último elemento da lista se nenhum índice for especificado
del lista[2] # a instrução del é usada para remover um item da lista pelo seu índice, o índice 2 corresponde ao valor 30
# lista.clear()
lista.insert(4, 3) # o método .insert(indice, valor) insere um valor em um indice específico, quando o índice é maior que o comprimento da lista, insert adiciona o item ao final
print(lista) # imprime o estado atual da lista, [10, 20, 40, 3]

lista.append(50) # adiciona 50 ao final
lista.pop() # remove o último elemento (50)
lista.append(60) # adiciona 60 ao final
lista.append(70) # adiciona 70 ao final
ultimo_valor = lista.pop(3) # quando um índice é fornecido a .pop(indice), ele remove e retorna o elemento nesse índice, o índice 3 na lista [10, 20, 40, 3, 60, 70]
print(lista, 'Removido,', ultimo_valor) # a lista fica sem o elemento removido, e é exibido o estado final da lista: [10, 20, 40, 60, 70] Removido, 3

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1,2,3] # a lista_a começa com [1, 2, 3]
lista_b = [4,5,6] # a lista_b começa com [4, 5, 6]
lista_c = [7,8,9] # a lista_c começa com [7, 8, 9]
lista_a.extend(lista_b) # o método .extend() é usado para adicionar todos os elementos de um iterável, (neste caso, lista_b) ao final da lista (lista_a)
lista_new = lista_a + lista_c # o operador + é usado para concatenar listas, neste ponto, lista_a é [1, 2, 3, 4, 5, 6], e lista_c é [7, 8, 9]
# a concatenação lista_a + lista_c resultará em [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_new) # imprime o conteúdo da lista_new

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2] # criação da lista_a com vários tipos de dados
lista_b = lista_a.copy() # o método .copy(), cria uma nova lista que é uma cópia rasa dos elementos da lista_a

lista_a[0] = 'Qualquer coisa' # aqui está modificando o elemento no índice 0 da lista_a para 'Qualquer coisa'
print(lista_a) # imprime ['Qualquer coisa', 'Maria', 1, True, 1.2]
print(lista_b) # imprime ['Luiz', 'Maria', 1, True, 1.2]












