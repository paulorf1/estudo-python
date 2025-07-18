"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo' # variavel a usar o fatiamento
print(variavel[::-1]) # inicio omitido, fim omitido, -1 faz com que o fatiamento ocorra de tras para frente
print(variavel[2::]) # inicia depois de 2 casas