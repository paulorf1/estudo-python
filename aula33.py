# https://docs.python.org/pt-br/3/library/stdtypes.html
# Imutáveis que vimos: str, int, float, bool

string = 'Paulo Ramos' # defini uma variavel com um nome
outra_variavel = f'{string[: 3]}ABC{string[4:]}' # combina fatiamento de string com concatenação usando uma f-string, string[:3] resulta em 'Pau' / 
# 'ABC': Esta é uma string literal que será inserida no meio / string[4:] resulta em 'o Ramos' / outra_variavel: 'PauABCo Ramos'
print(string) # imprime o valor original da variável string
print(outra_variavel) # imprime o resultado da manipulação
print(string.capitalize()) # o método .capitalize() retorna uma cópia da string com o primeiro caractere em maiúscula e o restante em minúscula
print(string.zfill(12)) # o método .zfill(largura) retorna uma cópia da string preenchida com caracteres '0' (zeros) à esquerda até atingir o largura total especificado