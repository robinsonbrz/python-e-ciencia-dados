def delete_lines(text):
    lines = text.split('\n')
    new_lines = []
    
    

    new_lines = [line for i, line in enumerate(lines) if (i+2) % 3 == 0]
    return '\n'.join(new_lines)

text = """
1. Introdução
1m
Reproduzir
2. Download e Instalação do Python
2m
Reproduzir
3. Instalação do Visual Studio Code
3m
Reproduzir
4. Layout da Tela
1m
Reproduzir
5. Sintaxe Básica em Python
"""

print(delete_lines(text))
