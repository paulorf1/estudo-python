# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True) #o operador 'and' retorna True somente se todos os valores (ou expressões) que ele conecta forem verdadeiros
#se houver qualquer valor False, como 0, None, string vazia '', etc, o 'and' resultará em False
print(True and 0 and True) #o primeiro operando (True) é verdadeiro, o segundo operando (0) é considerado "falso" (falsy), Como há um valor "falso" (0), o resultado do and será 0
#a avaliação para aqui e o 0 é retornado
print(True and None and True) #aqui retorna None