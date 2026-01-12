# map - para mapear dados
from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
        {'nome': 'produto 5', 'preco': 10.00},
        {'nome': 'produto 1', 'preco': 22.32},
        {'nome': 'produto 3', 'preco': 10.11},
        {'nome': 'produto 2', 'preco': 105.87},
        {'nome': 'produto 4', 'preco': 69.90},
    ]
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porceto = partial(aumentar_porcentagem, porcentagem=1.1)

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porceto(p['preco'])} 
#     for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {**produto, 'preco': aumentar_dez_porceto(produto['preco'])}

novos_produtos = map(
    muda_preco_de_produtos,
    produtos)

print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(list(novos_produtos))

print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType))

print(
    list(map(
        lambda x: x * 3, 
          [1,2,3,4]
    ))
)

