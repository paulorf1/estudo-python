"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0 # começa criando uma variável chamada contador, dá a ela o valor inicial de 0, essa variável vai "contar" quantas vezes o loop foi executado

while contador <= 10: # ele verifica a condição: 'enquanto o valor de contador for menor ou igual a 10'
    contador = contador + 1 # ela pega o valor atual de contador e adiciona 1 a ele, atualizando o próprio contador
    print(contador) # dentro do loop, esta linha exibe o novo valor de contador a cada iteração, depois que ele foi incrementado
print('Acabou') # linha fora do loop, ela só é executada depois que o loop while termina (quando contador se torna 11), fazendo com que contador <= 10 seja False