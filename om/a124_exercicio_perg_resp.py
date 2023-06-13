
# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_corretas = 0
for pergunta in perguntas:
    # exibir a questão
    print(pergunta.get("Pergunta"))
    # exibir opções
    for num_opcao, opcao in enumerate(pergunta.get("Opções")):
        print(f"{num_opcao}) {opcao}")
    # solicitar resposta do usuario
    resposta_escolhida = int(input("A escolha o opção correta de 0 a 3: "))
    # verificar resposta certa ou errada
    if pergunta.get("Opções")[resposta_escolhida] == pergunta.get("Resposta"):
        print("Resposta correta 👍 ✅")
        respostas_corretas += 1
    else:
        print("Resposta errada  👎 ⭕")
    print("________________________\n\n\n")

print(f"Você acertou {respostas_corretas} questões de {len(perguntas)}!")

# respostas_corretas = 0
# for numero, i in enumerate(perguntas):
#     # exibir a questão
#     print(perguntas[numero].get("Pergunta"))
#     # exibir opções
#     for num_opcao, opcao in enumerate(perguntas[numero].get("Opções")):
#         print(f"{num_opcao}) {opcao}")
#     # solicitar resposta do usuario
#     resposta_escolhida = int(input("A escolha o opção correta de 0 a 3: "))
#     # verificar resposta certa ou errada
#     if perguntas[numero].get("Opções")[resposta_escolhida] == perguntas[numero].get("Resposta"):
#         print("Resposta correta 👍 ✅")
#         respostas_corretas += 1
#     else:
#         print("Resposta errada  👎 ⭕")
#     print("________________________\n\n\n")

# print(f"Você acertou {respostas_corretas} questões !")