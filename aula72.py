# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplica (5, 2, 9, 2, 8)
print(multiplicacao)



# Crie uma função fala se um numero é par ou impar.
# Retorne se o numero é par ou ímpar.

def impar_par (numero):
    return numero % 2 == 0
print(impar_par(2))
print(impar_par(9))
print(impar_par(15))
print(impar_par(88))

# outro jeito
def impar_par (numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
print(impar_par(2))
print(impar_par(9))
print(impar_par(15))
print(impar_par(88))