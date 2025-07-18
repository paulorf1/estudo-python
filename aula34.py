"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True # você começa definindo uma variável booleana chamada condicao e a atribui como True

while condicao: # este é o início do loop while, significa 'enquanto a expressão condicao for verdadeira True', continue executando o bloco de código
    nome = input('Qual o seu nome: ') # dentro do looping o programa pede ao user digitar seu nome, e é armazenado na variavel nome
    print(f'Seu nome é: {nome}') # o nome que o user digitou é exibido 
    if nome == 'sair': # o programa verifica uma condição: se o valor da variável nome é exatamente igual à string 'sair'
        break # se a condição nome == 'sair' for True (ou seja, o usuário digitou 'sair' com 's' minúsculo), a instrução break é executada
print('Acabou') # o programa se encerra e exibe essa mensagem