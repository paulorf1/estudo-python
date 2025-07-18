"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

nome = 'Paulo Ramos' # string original que vamos iterar
indice = 0 # indice é iniciado em 0, o primeiro caractere de um string
novo_nome = '' # string vazia é criada, onde você vai construir o resultado
while indice < len(nome): # loop, ele continuará executando enquanto o valor de indice for menor que o comprimento total da string nome
    letra = nome[indice] # esta linha usa o indice atual para acessar um caractere especifico da string nome, ex: na primeira iteração, indice é 0, letra será 'P'
    novo_nome += f'*{letra}' # está linha concatena (adiciona) à novo_nome, cria uma string que começa com um asterisco * e seguida pela letra atual
    indice += 1 # a cada iteração o indice é incrementado em 1
novo_nome += '*' # depois que o loop termina, está linha adiciona um asterisco * final à novo_nome
print(novo_nome) # novo_nome com asteriscos é impressa