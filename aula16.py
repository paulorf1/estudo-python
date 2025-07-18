#if / elif / else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"?') #o que o usuário digitar (uma string) será armazenado na variável entrada
if entrada == 'entrar': #se a entrada for exatamente igual a 'entrar', o print abaixo é executado
    print('Você entou no sitema') #imprimi se entrada for = 'entrar'
elif entrada == 'sair': #se a entrada for exatamente igual a 'sair', o print abaixo é executado
    print('Você saiu do sistema') #imprimi se entrada for = 'sair'
else: #se nenhuma das opções forem digitadas, o print abaixo é executado
    print('Você não digitou nem entrar e nem sair.') #imprimi se entrada não for 'entrar' e nem 'sair'