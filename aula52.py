"""
Tipo tupla - Uma lista imutável
"""

"""Exemplo de tuple"""
nomes = 'Maria', 'Helena', 'Luiz' # quando você atribui múltiplos valores separados por vírgulas a uma única variável, sem usar colchetes [], você está criando uma tupla, tuplas são imutáveis
print(nomes[0]) # assim como nas listas, você pode acessar elementos de uma tupla usando indexação, nomes[0] refere-se ao primeiro elemento, que é 'Maria'
print(nomes) # imprime a tupla completa


"""Formas diferentes"""
nomes = ['Maria', 'Helena', 'Luiz'] # aqui, você redefine nomes, desta vez como uma lista (indicado pelos colchetes [])
nomes = tuple(nomes) # a função tuple() recebe um iterável (como uma lista) e retorna uma nova tupla com os elementos desse iterável, a variável nomes agora aponta para esta nova tupla
nomes = list(nomes) # a função list() recebe um iterável (como uma tupla) e retorna uma nova lista com os elementos desse iterável, a variável nomes agora aponta para esta nova lista
print(nomes[-1]) # está usando indexação negativa, acessa o último elemento da lista (ou tupla), [-2] o penúltimo, e assim por diante
print(nomes) # imprime o estado final da variável nomes, que é uma lista