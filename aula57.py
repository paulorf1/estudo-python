""" Lista de listas e seus índices """

salas = [ # uma lista principal chamada salas, salas[0] / salas[1] / salas[2] dentro de salas[2] no indice 3 há uma tupla (0,10,20,30,40)
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40) ],  # 2
]
print (salas[1][0]) # salas[1] acessa a segunda lista da principal, [0] acessa 'Elaine'
print (salas[0][1]) # salas[0] acessa a primeira lista da principal, [1] acessa 'Helena'
print (salas[2][2]) # salas[2] acessa a terceira lista da principal, [2] acessa 'Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)
print(salas[2][3][3]) # salas[2] acessa a terceira lista da principal, [3] acessa o quarto elemento, [3] acessa 30 da tupla
for sala in salas: #loop externo, itera sobre cada 'sala' (cada sub-lista) na lista principal salas
    print(f'A sala é: {sala}') # a cada iteração do loop externo, ele imprime a sub-lista completa
    for aluno in sala: # este é o loop interno, é executado para cada sala (sub-lista) que o loop externo está processando
        print(aluno) # imprime cada elemento individual