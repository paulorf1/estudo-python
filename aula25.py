"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
# nome = 'Paulo'
# preco = 1000.95897643
# variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %04X' % (15, 15))

nome = 'Luiz' #define uma string nome
preco = 1000.95897643 #defini um numero de ponto flutuante com varias casas decimais preco
variavel = '%s, o preço é R$%.2f' % (nome, preco) #'%s, o preço é R$%.2f': string de formato, % (nome, preco):o operador % funciona como um "aplicador de formato"
print(variavel) #exibe a string formatada
print('O hexadecimal de %d é %08X' % (1500, 1500)) #'O hexadecimal de %d é %08X': é a string de formato, % (1500, 1500) são pasasdos para preencher os especificadores %d e %08X