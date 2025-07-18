# Operador lógico "not"Add commentMore actions
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')

print(not True)  #se o valor for True, not o transforma em False
print(not False)  #se o valor for False, not o transforma em True


esta_chovendo = False #esta_chovendo é falso

if not esta_chovendo: #se não for isso, (e não é pois esta_chovendo = false) exibe
    print("Vamos sair para passear!")
else:
    print("É melhor ficar em casa.") #se esta_chovendo = true, exibiria esse