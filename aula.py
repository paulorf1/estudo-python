# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que
# questiona se um valor é igual a outro

print(10 == 10)  # pergunta se 10 é = a 10, como é verdade então é igual a True
print(10 == 11)  # pergunta se 10 é = a 11, como é falso então é igual a False
print(type(True)) # True é um valor booleano, então o Python irá imprimir <class 'bool'>
print(type(False)) # False é um valor booleano, então o Python irá imprimir <class 'bool'>
print(type(10 == 10)) # Primeiro avalia 10 == 10 que é True e depois o tipo que é booleano e imprime  <class 'bool'>
print(type(10 == 11)) # Primeiro avalia 10 == 11 que é False e depois o tipo que é booleano e imprime  <class 'bool'>