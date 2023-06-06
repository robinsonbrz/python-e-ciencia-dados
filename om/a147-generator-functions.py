# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        # yield é como um return
        # salva o estado anterior a cada next ou iteração
        yield n
        n += 1

        if n >= maximum:
            return
    # sempre que a função chega ao return
    # Lança a exceção StopIteration


gen = generator(maximum=10)
# pode-se chamar pelo next
print(f"Pelo next: {next(gen)}")
print(f"Pelo next: {next(gen)}")
for n in gen:
    # ou a cada chamada o generator sabe o estado anterior e avança
    print(n)
    print(f"Pelo next interno: {next(gen)}")