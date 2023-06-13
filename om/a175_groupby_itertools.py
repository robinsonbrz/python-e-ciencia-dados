from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

"""
A
{'nome': 'Luiz', 'nota': 'A'}    
{'nome': 'Fabrício', 'nota': 'A'}
{'nome': 'João', 'nota': 'A'}    
{'nome': 'André', 'nota': 'A'}   
B
{'nome': 'Letícia', 'nota': 'B'} 
{'nome': 'Eduardo', 'nota': 'B'} 
C
{'nome': 'Rosemary', 'nota': 'C'}
{'nome': 'Anderson', 'nota': 'C'}
D
{'nome': 'Joana', 'nota': 'D'}   

"""