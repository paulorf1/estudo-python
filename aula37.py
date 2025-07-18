"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0 # variavel contador é inicializada com 0

while contador <= 100: # o loop while continuará executando enquando o contador for menor ou igual a 100
    contador += 1 # em cada iteração do loop, o contador é incrementado em 1
    if contador == 6: # quando o contador se torna 6, o print a seguir é exibido
        print('Não vou mostrar o 6.') # quando o contador for 6 exibe
        continue # continue o looping
    if contador >= 10 and contador <= 27: # quando contador está entre 10 e 27 (inclusive) o print a seguir é exibido
        print('Não vou mostrar o', contador) # é exibido a mensagem + o numero do contador
        continue # continue o looping 
    print(contador) # esta linha só é executada se as condições if com continue não forem satisfeitas, ou seja, ela imprime os números que não foram "pulados"
    if contador == 40: # quando o contador se torna 40, a instrução break é executada, e saia do loop e exibe o print a seguir
        break
print('Acabou') # exibe esse print