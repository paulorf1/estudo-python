"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

condicao = False # variavel condicao é false, isso determina o caminho do if/else
passou_no_if = None # a variavel passou_no_if é none, representa a 'ausencia de um valor' ou valor nulo, que ainda não receberam um valor

if condicao: # o python verifica se é True, como ela é definida como False, não a executa
    passou_no_if = True
    print('Faca algo')
else: # como o if foi falsa, esse bloco é executado com o print a seguir, e passou_no_if = True, faz ele continuar None
    print('Não faça algo')

if passou_no_if is None: # o operador is verifica se as variaveis referem-se ao mesmo objeto, passou_no_if ainda é None, portanto a condição None is None é True
    print('Não passou no if') # essa mensagem será impressa

if passou_no_if is not None: # verifica se a variavel passou_no_if ´não é None', como passou_no_if é None (False)
    print('Passou no if') # esse bloco não será impresso

print(passou_no_if, passou_no_if is None) # imprime o valor atual de passou_no_if, que é None e imprime o resultado da comparação None is None, que é True
print(passou_no_if, passou_no_if is not None) # imprime o valor atual de passou_no_if, que é None e imprime o resultado da comparação None is Not None, que é False
 



# passou_no_if = None

# if condicao:
#     passou_no_if = True
#     print('Faça algo')
# else:
#     print('Não faça algo')

# if passou_no_if is None:
#     print('Não passou no if')
# else:
#     print('Passou no if')