# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD' # uma string, que é sequência ordenada e imutável de caracteres
lista = ['Maria', 'Helena',1, 2, 3, 'Eduarda'] # lista mutavel, você pode adicionar, remover ou modificar seus elementos
tupla = 'Python', 'é', 'legal' # isso define uma tupla, que é semelhante a uma lista, mas é imutável
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
] # isso cria uma lista aninhada, é uma lista onde cada elemento é, por si só, outra lista

a, b, c, *_ = lista # essa linha desempacota a lista em várias variáveis, a recebe 'Maria', b > 'Helena', c > 1, *_ é um operador especial que "coleta" o restante dos elementos da lista
print(a, c) # isso imprime os valores de a 'Maria' e c 1

p, b, *_, ap, u = lista # essa linha desempacota a lista, p recebe 'Maria', b > 'Helena', ap > o penultimo elemento (3), u > o ultimo elemento 'Eduarda'
print(p, u, ap) # isso imprime os valores de p 'Maria', u 'Eduarda' e ap (3)

print(*lista) # isso desempacota todos os elementos da lista, e os passa como argumentos separados para a função print(), a saída será: Maria Helena 1 2 3 Eduarda
print(*string) # da mesma forma, isso desempacota cada caractere da string e os imprime separadamente: A B C D
print(*tupla) # isso desempacota a tupla e imprime seus elementos: Python é legal
print(*salas, end='\n') # desempacota a lista salas, cada sub lista se torna um argumento separado para o print(), o end='\n' garante que uma nova linjha seja adicionada ao final da saida
# a saida será algo com espaços entre as linhas impressas
print(*salas, sep='\n') # desempacota a lista salas, mas o argumento sep='\n' instrui a função print() a usar um caractere de nova linha como separador entre os argumentos
#isso faz com que cada sublista seja impressa em uma nova linha