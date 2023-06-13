# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
]

print_iter(combinations(pessoas, 2))
"""
('João', 'Joana')
('João', 'Luiz')
('João', 'Letícia')
('Joana', 'Luiz')
('Joana', 'Letícia')
('Luiz', 'Letícia')
"""

print_iter(permutations(pessoas, 2))
"""
('João', 'Joana')
('João', 'Luiz')
('João', 'Letícia')
('Joana', 'João')
('Joana', 'Luiz')
('Joana', 'Letícia')
('Luiz', 'João')
('Luiz', 'Joana')
('Luiz', 'Letícia')
('Letícia', 'João')
('Letícia', 'Joana')
('Letícia', 'Luiz')
"""
print_iter(product(*camisetas))
"""
('preta', 'p', 'masculino')
('preta', 'p', 'feminino')
('preta', 'm', 'masculino')
('preta', 'm', 'feminino')
('preta', 'g', 'masculino')
('preta', 'g', 'feminino')
('branca', 'p', 'masculino')
('branca', 'p', 'feminino')
('branca', 'm', 'masculino')
('branca', 'm', 'feminino')
('branca', 'g', 'masculino')
('branca', 'g', 'feminino')
"""