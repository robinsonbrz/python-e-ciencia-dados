


nome = input('Digite seu primeiro nome :  ')

try:
    if len(nome) <= 4:
        print(f'{nome} Seu nome é curto!')
    elif len(nome) > 4 and len(nome) <= 6:
        print(f'{nome} Seu nome é normal!')
    else:
        print(f'{nome} Seu nome é muito grande!')
except:
    print("Houve um erro na validação.")