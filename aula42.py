frase = 'O Python é uma linguagem de programação ' \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.' # a string frase é definida, usou barras invertidas \ para quebrar a string em várias linhas
i = 0 # o índice para percorrer a frase
qtd_apareceu_mais_vezes = 0 # essa variável guardará a maior contagem de ocorrências que encontramos até o momento
letra_apareceu_mais_vezes = '' # esta variável guardará a letra correspondente à: qtd_apareceu_mais_vezes, ela começa vazia 

while i < len(frase): # loop principal que itera sobre cada caractere da frase usando o indice (i)
    letra_atual = frase[i] # em cada iteração, o caractere na posição i é atribuído a letra_atual

    if letra_atual == ' ': # verifica se o caractere atual é um espaço
        i += 1 # incrementa o índice para não ficar preso no espaço
        continue # faz com que o Python pule o restante do código na iteração atual, e vá diretamente para a próxima iteração do loop while

    qtd_atual = frase.count(letra_atual) # para cada letra_atual (que não é um espaço), o método .count() é chamado, e retorna o número de vezes que a substring (neste caso, a letra_atual) aparece na frase inteira

    if  qtd_apareceu_mais_vezes < qtd_atual: # compara a contagem atual (qtd_atual) com a maior contagem que já foi registrada (qtd_apareceu_mais_vezes
        qtd_apareceu_mais_vezes = qtd_atual # a maior contagem é atualizada
        letra_apareceu_mais_vezes = letra_atual # a letra correspondente é registrada

    i += 1 # o índice é incrementado para mover para o próximo caractere

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
) # após o loop terminar (quando todos os caracteres da frase foram verificados), a mensagem final é impressa