"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>fAdd 
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC' #define uma string simples 'ABC' na variável 'variavel'
print(f'{variavel}') #forma mais simples de usar uma f-string: apenas insere o valor da variável
print(f'{variavel: >10}') # >: alinha o texto à direita, 10: define a largura total do campo
print(f'{variavel: <10}.') # <: alinha o texto à esquerda, 10: define a largura total do campo
print(f'{variavel: ^10}.') # ^: centraliza o texto, 10: define a largura total do campo
print(f'{1000.4873648123746:0=+10,.1f}') # :: Inicia a especificação de formato, 0: caractere de preenchimento, =: força o sinal a ficar antes dos zeros de preenchimento
# +: força a exibição do sinal (+ ou -) mesmo para números positivos, 10 largura do campo, , adiciona separador de milhares, .1f, formata como um numero flutuante
print(f'O hexadecimal de 1500 é {1500:08X}') #:: inicia a especificação de formato, 0: preenche com zeros à esquerda, 8: largura total do campo
# X: Converte o número para hexadecimal (letras maiúsculas)
print(f'{variavel!r}') # !r: uma conversão de representação, retorna a representação 'oficial' da string, incluindo as aspas