# if / elif      / else
# se / se não se / se não

condicao1 = True #criação da variavel condicao1 (booleanas) com valor True, para controlar o fluxo dos blocos if/elif
condicao2 = True #criação da variavel condicao1 (booleanas) com valor True, para controlar o fluxo dos blocos if/elif
condicao3 = True #criação da variavel condicao1 (booleanas) com valor True, para controlar o fluxo dos blocos if/elif
condicao4 = True #criação da variavel condicao1 (booleanas) com valor True, para controlar o fluxo dos blocos if/elif

if condicao1: #O Python verifica se condicao1 é True, como é True, esta condição é verdadeira e exibira o print abaixo, e não verifica 
    # e nem executa nenhuma das outras opções (só o que está 'fora' do bloco de if/ elif / else)
    print('Código para condição 1') 
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')
if 10 == 10:
    print('Outro if')
    
print('Fora do if')