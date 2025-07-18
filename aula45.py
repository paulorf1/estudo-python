"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# Isso que o For faz
texto = 'Paulo' # a string que vai iterar
iteratador = iter(texto) # a função iter() recebe um objeto iterável, e retorna um objeto iterador

while True: # loop infinito que tem a intenção de continuar chamadando next(), até que não haja mais item
    try: 
        letra = next(iteratador) # a função next() é chamada no objeto iteratador, ela tenta pegar o próximo item na sequência
        print(letra) # se houver um próximo item, ele é retornado e atribuído a letra
    except StopIteration: # se não houver mais itens, next() levanta uma exceção especial chamada StopIteration, este bloco captura a exceção StopIteration
        break # uma vez que StopIteration é capturada, a instrução break é executada, encerrando o loop while

for letra in texto: # maneira idiomática e recomendada de iterar sobre a maioria das sequencias, chama iter() no texto, chama next() repetidamente no iterador, e  lida com a exceção StopIteration automaticamente
    print(texto) # dentro deste loop, você está imprimindo a string completa
