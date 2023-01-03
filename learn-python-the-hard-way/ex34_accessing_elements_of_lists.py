'''
ex34-accessing-elements-of-lists
'''

animals = [ 'bear' , 'python3.6' , 'peacock' , 'kangaroo' , 'whale' , 'platypus' ]

def responde_posicao_lista(lista, posicao):
    return lista[posicao]

while True:
    try:
        posicao_pergunta = int(input("Digite um número de 0 a , ou 99 para sair:\n>"))
        if posicao_pergunta == 99:
            print("Selecionado 99. Finalizando execução\n")
            break
        elif posicao_pergunta < 0 or posicao_pergunta > len(animals)-1:
            print("O número é inválido tente novamente\n")
        else:
            print( f"A string na posição {posicao_pergunta} é: ", responde_posicao_lista(animals, posicao_pergunta), "\n")
        
    except ValueError:
        print("É necessário digitar um número inteiro. \nTente novamente\n")




# 1. The animal at 1.
# 2. The third (3rd) animal.
# 3. The first (1st) animal.
# 4. The animal at 3.
# 5. The fifth (5th) animal.
# 6. The animal at 2.
# 7. The sixth (6th) animal.
# 8. The animal at 4.

