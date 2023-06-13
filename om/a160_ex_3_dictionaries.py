# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Imprima produtos_ordenados_por_nome e produtos_ordenados_por_preco# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)


for produto in produtos:
    print(produto["preco"])
    produto["preco"] = produto["preco"]*1.1
    print(produto["preco"])
import copy

novos_produtos = copy.deepcopy(produtos)
produtos_ordenados_por_preco = copy.deepcopy(produtos)

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda produto: produto["nome"], reverse=True)
produtos_ordenados_por_preco.sort(key=lambda produto: produto["preco"])
print("##########################\nProdutos")
print(produtos)
print("##########################\nNovos Produtos")
print(novos_produtos)
print("##########################\nProdutos ordenados nome")
print(produtos_ordenados_por_nome)
print("##########################\nProdutos ordenados preco")
print(produtos_ordenados_por_preco)