"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

qtd_linhas = 5 # defini quantas linhas terá sua grade
qtd_colunas = 5 # defini quantas colunas terá sua grade

linha = 1 # a variavel linha, começa em 1
while linha <= qtd_linhas: # o loop é responsavel por iterar sobre cada linha, ele continuará enquanto o valor de linha for menor ou igual a qtd_linhas
      coluna = 1 # a cada nova iteração do loop, a variavel coluna é reinicializada para 1, ele continuará enquanto o valor de coluna for menor ou igual a qtd_colunas
      while coluna <= qtd_colunas: # loop interno: enquanto 'coluna' for menor ou igual à 'qtd_colunas'
             print(f'{linha = }, {coluna = }') # imprime os valores atuais de linha e coluna
             coluna += 1 # loop interno, coluna é incrementada em 1, uma vez que coluna excede qtd_colunas, o loop interno termina
      linha += 1 # loop externo, após o loop interno ter sido completamente executado para a linha atual, a linha é incrementada em 1
print('Acabou') # esta linha só é executada depois que o loop externo termina, significando que todas as linhas e colunas foram processadas