"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

# frase = 'Olha só que, coisa interessante'
# lista_frases = frase.split()
# print(lista_frases)

# frase = 'Olha só que, coisa interessante'
# lista_frases = frase.split(',')
# print(lista_frases)

frase = 'Olha só que, coisa interessante' # define a string original
lista_frases = frase.split(',') # o método .split(',') divide a string frase em uma lista de substrings, usando a vírgula , como delimitador
lista_frases_cruas = frase.split(',')  # você cria uma cópia idêntica da lista gerada na linha anterior, Ambas as variáveis apontam para a mesma lista neste momento

lista_frases = [] # você redefine a variável lista_frases para uma lista vazia, a lista criada no passo 2 é perdida, a menos que outra variável ainda a referencie
for i, frase in enumerate(lista_frases_cruas): # este loop for itera sobre a lista_frases_cruas, enumerate() fornece tanto o (i) quanto o valor (frase_item_crua) de cada elemento
    lista_frases.append(lista_frases_cruas[i].strip()) # .strip(): este método remove todos os espaços em branco do inicio e do final da string, .append(): o resultado da operação strip() é adicionado à nova lista lista_frases que você inicializou como vazia 
    # lista_frases[i] = lista_frases[i].strip  
    # # print(lista_frases[i].strip())  
    # # print(lista_frases[i].rstrip())  
    # # print(lista_frases[i].lstrip())  
    # # print(lista_frases_cruas)
    # # print(lista_frases)
frases_unidas = '-'.join(lista_frases) # o método .join() é usado para concatenar elementos de um iterável (sua lista_frases) em uma única string, o separador ('-' neste caso) é a string sobre a qual você chama o método, ele é inserido entre cada elemento da lista
print(frases_unidas) # imprime a string final