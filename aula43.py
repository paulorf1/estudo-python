# Exemplo 1
texto = 'Python' # string origin que sera processada
novo_texto = '' # string vazia é criada, será usada para criar a nova string 
for letra in texto: # looping for, ideal para iterar diretamente sobre os elementos de uma sequência
    novo_texto += f'*{letra}' # esta linha está concatenando (adicionando) conteúdo à novo_texto
    print(letra) # dentro do loop, esta linha imprime o caractere atual (letra) a cada iteração
print(novo_texto) # fora do loop, ela só será executada depois que o loop for tiver terminado, e imprime a string completa que foi construída novo_texto


# Exemplo 2
texto = 'Python' # string origin que sera processada

i = 0 # a variável i é inicializada como 0
tamanho_string = len(texto) # a função len() retorna o número de caracteres na string texto
while i < tamanho_string: # loop while, ele continuará executando enquanto o valor de i for menor que tamanho_string (nesse caso 6)
    print(texto[i], i) # acessa o caractere da string texto na posição especificada por [i], e imprime valor atual do indice i
    i +=1 # esta linha incrementa o valor de i em 1

# Exemplo 3
senha_salva = '123456' # define a senha "correta" que o programa espera que o usuário digite
senha_digitada = '' # inicializa a variável senha_digitada como uma string vazia, no início, a senha_digitada (vazia) é diferente da senha_salva ('123456'), isso garante que o loop while comece a executar pelo menos uma vez
repeticoes = 0 # inicializa um contador para registrar quantas vezes o usuário tentou digitar a senha

while senha_salva != senha_digitada: # loop while, ele verifica a condição "enquanto a senha_salva for diferente de senha_digitada"
    senha_digitada = input(f'Sua senha ({repeticoes}x): ') # dentro do loop, o programa solicita ao usuário que digite a senha, e mostra o número da tentativa atual

    repeticoes += 1 # a cada vez que o loop executa, o contador repeticoes é incrementado em 1

print(repeticoes) # após o loop terminar, imprime o número total de tentativas
print('Aquele laço acima pode ter repetições infinitas') # se a senha não for acertada o programa continua para sempre