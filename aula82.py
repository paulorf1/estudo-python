def executa(funcao, *args):
    return funcao(*args)

#Exemplo utilizando lambda
print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)



def soma(x, y):
    return x + y

#Exemplo utilizando lambda
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
    executa(soma, 2, 3),
    soma (2, 3)
)



def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#Exemplo utilizando lambda
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))