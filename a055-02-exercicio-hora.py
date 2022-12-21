"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

a = input('Digite a hora atual entre 0 e 23:  ')

try:
    inteiro = int(a)
    if inteiro >= 0 and inteiro <= 11:
        print(f'{a} Bom dia!')
    elif inteiro > 11 and inteiro <= 17:
        print(f'{a} Boa tarde!')
    elif inteiro > 17 and inteiro <= 23:
        print(f'{a} Boa noite!')
    else:
        print(f'{a} Não é um horário válido')
except:
    print(f'###{a} não é um número inteiro válido ###')