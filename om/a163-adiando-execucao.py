# Exercício - Adiando execução de funções
# somente executa apos o clojure

def sum(x, y):
    return x + y


def multiply(x, y):
    return x * y


def create_function(function, x):
    def internal(y):
        return function(x, y)
    return internal


sum_plus_five = create_function(sum, 5)
multiply_by_ten = create_function(multiply, 10)

print(sum_plus_five(10))
print(multiply_by_ten(10))