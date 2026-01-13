# Jogo de adivinhação de palavra para praticar loops e controle de tentativas.

import os # O módulo os é importado para permitir a interação com o sistema operacional
palavra_secreta = 'microsoft' # defini a palavra que o user deve adivinhar
letras_acertadas = '' # string vazia para armazenar as letrar que o user digitou corretamente
numero_tentativas = 0 # um contador para saber quantas tentativas foram feitas

while True: # loop infinito que continuará pedingo letras até o jogador acertar
 
    letra_digitada = input('Digite uma letra: ') # pede uma letra ao jogador
    numero_tentativas += 1 # increment o contador a cada tentativa

    if len(letra_digitada) > 1: # valida se o user digitou mais de uma letra, se sim, imprime uma mensagem de erro e usa continue
        print('Digite apenas uma letra') # mensagem de erro
        continue # continua 

    if letra_digitada in palavra_secreta: # verifica se a letra_digitada existe em palavra_secreta
        letras_acertadas += letra_digitada # se a letra estiver na palavra secreta, ela é adicionada à string letras_acertadas

    palavra_formada = '' # a cada nova tentativa, esta variável é resetada
    
    for letra_secreta in palavra_secreta: # um loop for interno percorre cada caractere da palavra_secreta original
        if letra_secreta in letras_acertadas: # para cada letra da palavra_secreta, verifica se ela está presente na coleção de letras_acertadas
            palavra_formada += letra_secreta # se sim, a letra real é adicionada a palavra_formada
        else: # se não
            palavra_formada += '*' # um asterisco é adicionado, ocultando a letra
    print('Palavra formada: ', palavra_formada) # exibe o progresso, como *i*t*n*n**do
    
    if palavra_formada == palavra_secreta: # verifica se a palavra formada (com as letras já adivinhadas) é idêntica à palavra_secreta, se sim o user venceu
        os.system('cls') # limpa a tela do console, para uma mensagem de vitória mais limpa
        print('Você acertou, Parabéns!') # mensagem de vitória exibida
        print('A palavra era', palavra_secreta) # mostra a palavra completa
        print('Tentativas', numero_tentativas) # mostra quantas tentativas foram gastas
