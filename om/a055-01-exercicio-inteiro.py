"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

a = input('Digite um numero inteiro:  ')

try:
    inteiro = int(a)
    if inteiro % 2 == 0:
        print(f'{a} é um número inteiro Par')
    else:
        print(f'{a} é um número inteiro Ímpar')
except:
    print(f'###{a} não é um número inteiro válido ###')
