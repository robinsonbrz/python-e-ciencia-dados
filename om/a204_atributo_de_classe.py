# Atributos de classe
# ano atual é compartilhado com todas as instâncias
# mesmo que não tenha sido instanciada
# pode-se acessar pelo nome da classe

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

print(Pessoa.ano_atual)
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p1.ano_atual)
print(p2.ano_atual)