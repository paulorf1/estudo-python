""""""

for i in range(10): # este loop principal faz com que a variável i assuma valores de 0 a 9
    if i == 2: # se o i for igual a 2
        print('i é 2, pulando...') # mensagem será impressa
        continue # faz com que o python pule o restante do código e vai para proxima iteração
    if i == 8: # se o i for igual a 8
        print('i é 8, seu else não executará') # mensagem será impressa
        break # faz o python sair do loop for 
    for j in range(1,3): # este loop é executado para cada valor de i exceto quando i é 2 ou 8
        print(i,j) # imprime o par de valores atual de i e j
    else: # associado ao for j - o loop interno
        print('For completo com sucesso!') # como o for j in range(1, 3), não tem um break, ele sempre completará a iteração e esse print sempre será exibido