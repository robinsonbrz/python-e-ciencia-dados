# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134


call1 = CallMe('23945876545')
print(call1.phone)
retorno = call1('Luiz Otávio')
print(retorno)
call1.__call__("Nome")
print(retorno)

''' Resultado
23945876545
Luiz Otávio está chamando 23945876545
2134
Nome está chamando 23945876545
2134
'''