'''
Names, Variables, Code, Functions

Métodos são associados a classes
Funções são independentes de classe

Em Python, um método é um tipo de função que é definida dentro de uma classe
 e é usada para operar em dados contidos na própria classe . 

Função é um bloco de código que realiza uma tarefa específica e 
pode ser chamada de vários lugares no código.
'''

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"\n\n\arg1: {arg1}, arg2: {arg2}\n")

def print_any_qt_parameters(*args):
    for i, arg in enumerate(args):
        print(f"arg{i} = {arg}")

def print_any_qt_parameters_comprehension(*args):
    [print(i, " ", arg) for i, arg in enumerate(args)]


print_two("Robinson", "Enedino")

print_any_qt_parameters("arg1","arg2","arg3","arg4","arg1","arg2","arg3","arg4","arg1","arg2","arg3","arg4")

print_any_qt_parameters_comprehension("arg1","arg2","arg3","arg4","arg1","arg2","arg3","arg4","arg1","arg2","arg3","arg4")