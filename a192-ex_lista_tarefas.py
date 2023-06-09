# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# Nada a desfazer
# Nada a refazer

# Adicionar tarefa  # Utilizar list.insert(ponteiro, "string") 
# Comandos: listar, desfazer, refazer, clear

# lista de strings tarefas
######################3

import os

tarefas = {
    'tarefa':[],
    'ponteiro':0
    }

entrada_usuario = ''

def listar(tarefas):
    os.system('clear')
    lista = tarefas["tarefa"][:tarefas["ponteiro"]]
    # :tarefas["ponteiro"]
    if len(lista) > 0:
        [print(f'{i :2}:{tarefa}') for i, tarefa in enumerate(lista)] 
    else:
        print("Lista sem tarefas.")


def desfazer(tarefas):
    if tarefas['ponteiro'] > 0:
        tarefas['ponteiro']-=1
        listar(tarefas)
    else:
        listar(tarefas)
        print("Não há mais tarefas para desfazer")


def refazer(tarefas):
    if tarefas['ponteiro'] < len(tarefas["tarefa"]):
        tarefas['ponteiro']+=1
        listar(tarefas)
    else:
        listar(tarefas)
        print("Não há mais tarefas para refazer")
    


os.system('clear')
while entrada_usuario != 's':

    entrada_usuario = input('''\tDigite s para sair.
    \tAdicione uma tarefa na lista.
    \tComandos, l listar, d desfazer, r refazer.
    \tDigite uma tarefa ou comando:''')

    if entrada_usuario == 's':
        exit()
    if entrada_usuario == 'l':
        listar(tarefas)
    elif entrada_usuario == 'd':
        desfazer(tarefas)
    elif entrada_usuario == 'r':
        refazer(tarefas)
    else:
        tarefas['tarefa'].insert(tarefas['ponteiro'], entrada_usuario)
        tarefas['ponteiro'] += 1 
        listar(tarefas)




