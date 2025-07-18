""" while/else """
string = 'Valor qualquer' # string que será analisada é definida
 
i = 0 # O índice i é inicializado em 0, apontando para o primeiro caractere da string
while i < len(string): # looping principal, ele continuará executando enquanto o i for menor que o comprimeito da string (no caso 14)
    letra = string[i] # dentro do loop, o caractere na posição atual do i é atribuído à variável letra

    if letra == ' ': # ele verifica se a letra atual é um espaço em branco
        break # se letra for um espaço, a instrução break é executada

    print(letra) # se letra não for um espaço, ela é impressa
    i += 1 # o i é incrementado para passar para o próximo caractere
else: # este bloco else só é executado se o loop while completar todas as suas iterações sem que o break seja acionado
    print('Não encontrei um espaço na string.') # se não houver espaço na string, esse print é exibido
print('Fora do while.') # esta linha está fora tanto do while quanto do else associado a ele, ela sempre será executada depois que o loop