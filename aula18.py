# if / elif      / else
# se / se não se / se não

condicao1 = False #criação da variavel condicao1 com valor False, para controlar o fluxo dos blocos if/elif
condicao2 = False #criação da variavel condicao2 com valor False, para controlar o fluxo dos blocos if/elif
condicao3 = True  #criação da variavel condicao3 com valor True, para controlar o fluxo dos blocos if/elif
condicao4 = True  #criação da variavel condicao4 com valor True, para controlar o fluxo dos blocos if/elif

if condicao1: #o Python verifica se condicao1 é True, como condicao1 é False, esta condição não é satisfeita, não executa o bloco e vai para a proxima
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2: #o Python verifica se condicao1 é True, como condicao2 é False, esta condição não é satisfeita, não executa o bloco e vai para a proxima
    print('Código para condição 2')
elif condicao3: #o Python verifica se condicao3 é True, como condicao3 é True, esta condição é satisfeita, o print abaixo será executado
    print('Código para condição 3')
elif condicao4: #uma vez que uma condição em uma cadeia if/elif/else é satisfeita, o Python sai de toda a cadeia condicional
    print('Código para condição 4') #ignorado
else:
    print('Nenhuma condição foi satisfeita.') #ignorado

if 10 == 10: #este é um novo e independente if, sua execução não depende do que aconteceu na cadeia if/elif/else anterior
    print('Outro if') #portanto esse print sera executado

print('Fora do if') #também sera executado