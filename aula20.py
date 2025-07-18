""""""
primeiro_valor = input('Digite um valor: ') #a função input() pede ao usuário para digitar primeiro_valor, que sera uma string
segundo_valor = input('Digite outro valor: ') #a função input() pede ao usuário para digitar segundo_valor, que sera uma string

if primeiro_valor >= segundo_valor: #quando compara strings usando operadores >, <, >=, <=, o Python faz uma comparação  lexicográfica 
#ou (alfabética), ele compara os caracteres um a um, com base na ordem de seus códigos, ex: '20' é maior que '100', porque '2' é maior que '1' 
    print(f'{primeiro_valor=} é maior ou igual 'f' ao que {segundo_valor}') #se primeiro_valor for >= imprimi esse print
else:
    print(f'{segundo_valor=} é maior 'f' do que {primeiro_valor}') #imprimi esse print