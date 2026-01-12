# copy, sorted, produtos.sort
# Exercícios

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
novos_produtos = [
{**produto, 'preco': round(produto['preco'] * 1.1, 2)}
for produto in produtos
]
print('Produtos com o preço aumentado')
print(*novos_produtos, sep='\n')

print()

# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)
print('Lista original (produtos):')
print(*produtos, sep='\n')
print('\nNova lista (novos_produtos):')
print(*novos_produtos, sep='\n')

print()

# Ordene os produtos por nome decrescente (do maior para menor)
produtos_ordenados = sorted(produtos, key=lambda produto: produto['nome'], reverse=True)
print('Produtos ordenados maior para menor')
print(*produtos_ordenados, sep='\n')

print()

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
copia_produtos_ordenados_por_nome = copy.deepcopy(produtos_ordenados)
print('Copia produtos ordenados por nome')
print(*copia_produtos_ordenados_por_nome, sep='\n')

print()

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_preco = sorted(produtos, key=lambda produto: produto['preco'])
print('Produtos ordenados por preço')
print(*produtos_ordenados_por_preco, sep='\n')

print()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
copia_produtos_ordenados_por_preco = copy.deepcopy(produtos_ordenados_por_preco)
print('Copia produtos ordenados por preço')
print(*copia_produtos_ordenados_por_preco, sep='\n')




# solução do professor 
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')