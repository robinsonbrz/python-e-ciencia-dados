# não é possível importar mais de uma vez um módulo
# com exceção de utilizando a biblioteca importlib

import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')