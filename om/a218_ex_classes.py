# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro():
    def __init__(self, nome, Motor):
        self.nome = nome
        self.motor = Motor

class Motor():
    def __init__(self, nome):
        self.nome = nome

class Fabricante():
    def __init__(self, nome):
        self.nome = nome
        self._carros = []

    def listar_carros(self):
        return [carro.nome for carro in self._carros]
    
    def inserir_carro(self, Carro):
        self._carros.append(Carro)

f1 = Fabricante("Volks")
f2 = Fabricante("Fiat")
m1 = Motor("motor 1.3")
c1 = Carro("Fusca",m1)
c2 = Carro("Variant",m1)
f1.inserir_carro(c1)
f1.inserir_carro(c2)
print(f"Fabricante: {f1.nome} \nCarros:{f1.listar_carros()}")
print(f"c1.nome: {c1.nome} \nc1.motor.nome: {c1.motor.nome}\n\n")
print(f"c2.nome: {c2.nome} \nc2.motor.nome: {c2.motor.nome}\n\n")



# # # # # Exercício com classes
# # # # # 1 - Crie uma classe Carro (Nome)
# # # # # 2 - Crie uma classe Motor (Nome)
# # # # # 3 - Crie uma classe Fabricante (Nome)
# # # # # 4 - Faça a ligação entre Carro tem um Motor
# # # # # Obs.: Um motor pode ser de vários carros
# # # # # 5 - Faça a ligação entre Carro e um Fabricante
# # # # # Obs.: Um fabricante pode fabricar vários carros
# # # # # Exiba o nome do carro, motor e fabricante na tela
# # # # class Carro:
# # # #     def __init__(self, nome):
# # # #         self.nome = nome
# # # #         self._motor = None
# # # #         self._fabricante = None

# # # #     @property
# # # #     def motor(self):
# # # #         return self._motor

# # # #     @motor.setter
# # # #     def motor(self, valor):
# # # #         self._motor = valor

# # # #     @property
# # # #     def fabricante(self):
# # # #         return self._fabricante

# # # #     @fabricante.setter
# # # #     def fabricante(self, valor):
# # # #         self._fabricante = valor


# # # # class Motor:
# # # #     def __init__(self, nome):
# # # #         self.nome = nome


# # # # class Fabricante:
# # # #     def __init__(self, nome):
# # # #         self.nome = nome


# # # # fusca = Carro('Fusca')
# # # # volkswagen = Fabricante('Volkswagen')
# # # # motor_1_0 = Motor('1.0')
# # # # fusca.fabricante = volkswagen
# # # # fusca.motor = motor_1_0
# # # # print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

# # # # gol = Carro('Gol')
# # # # gol.fabricante = volkswagen
# # # # gol.motor = motor_1_0
# # # # print(gol.nome, gol.fabricante.nome, gol.motor.nome)

# # # # fiat_uno = Carro('Uno')
# # # # fiat = Fabricante('Fiat')
# # # # fiat_uno.fabricante = fiat
# # # # fiat_uno.motor = motor_1_0
# # # # print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

# # # # focus = Carro('Focus Titanium')
# # # # ford = Fabricante('Ford')
# # # # motor_2_0 = Motor('2.0')
# # # # focus.fabricante = ford
# # # # focus.motor = motor_2_0
# # # # print(focus.nome, focus.fabricante.nome, focus.motor.nome)