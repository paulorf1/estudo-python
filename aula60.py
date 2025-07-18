"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 10 # variavel booleana, 10 é igual a 10, condição recebera o valor True
variavel = 'Valor' if condicao else 'Outro valor' # expressão condicional, se condicao for True (que é) a variavel recebe 'valor', se condicao fosse False, receberia 'outro valor'
print(variavel) # imprime o valor da variavel (valor)


digito = 10  # > 9 = 0 # a variavel digito é inicializada com o valor 10
novo_digito = digito if digito <= 9 else 0 # aqui, a condição é digito <= 9, como 10 não é menor ou igual a 9 (é false), novo_digito recebe o valos após o else, que é 0
novo_digito = 0 if digito > 9 else digito  # a condição é digito > 9, como 10 é maior que 9 (é True), novo_digito recebe o valor antes do if que é 0
print(novo_digito) # imprime o valor final de novo_digito que será 0


print('Valor' if False else 'Outro valor' if False else 'Fim') # 'Valor' if False else... a primeira condição (False) é falsa, então o Python move-se para a parte else, que é outra expressão ternária,
# 'Outro valor' if False else 'Fim', nesta segunda expressão: a condição (False) é falsa novamente, então o valor final retornado é o que vem depois do else mais interno, que é 'Fim'