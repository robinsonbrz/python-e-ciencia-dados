import uma_linha
import documentando_funcoes

print(dir(uma_linha))
print('\n\n\n')
print('DOCUMENTAÇÃO ', uma_linha.__doc__)
print('\n\n\n')
print('Nome do módulo', uma_linha.__name__)
print('\n\n\n')
print('Package', uma_linha.__package__)
print('\n\n\n')
print('Caminho Arquivo completo', uma_linha.__file__)                          
print('\n\n\n')
print('dict', uma_linha.__dict__)
print('\n\n\n')

# print('help', uma_linha.__help__)
help(documentando_funcoes)