"""
Introdução ao desempacotamento
"""

nomes = ['Maria', 'Helena', 'Luiz'] # cria uma lista chamada nomes com três strings
print(nomes) # quando imprime uma lista diretamente em Python, ela é exibida com os colchetes [], e os elementos separados por vírgulas e espaços

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz', 'Teste'] # esta linha é um excelente exemplo de desempacotamento de sequência, o _ é usado como um nome de variável quando você precisa capturar um valor
# mas não pretende usá-lo mais tarde, é um "placeholder" para valores que você quer ignorar, o primeiro _ recebe 'Maria', o segundo _ recebe 'Helena', nome: Esta variável recebe o terceiro elemento da lista, que é 'Luiz'
# *resto: o operador *, quando usado no desempacotamento, coleta todos os elementos restantes da sequência em uma nova lista, que no caso é 'Teste'
print(nome, resto) # imprime o valor da variável nome, e o valor da variável resto: Luiz (Teste)