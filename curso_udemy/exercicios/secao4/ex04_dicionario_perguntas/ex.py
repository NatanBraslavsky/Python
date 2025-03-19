perguntas = [
    {
        'Pergunta' : 'Quanto é 2x2?',
        'Opções' : ['2', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5x5?',
        'Opções' : ['25', '5', '30', '45'],
        'Resposta' : '25',
    },
     {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4', '2', '10', '5'],
        'Resposta' : '5',
    },
]
qtd_acertos = 0
for pergunta in perguntas:
    print(f'{pergunta['Pergunta']}')
    opcoes = pergunta['Opções']
    for i,chave in enumerate(pergunta['Opções']):
        print(f'{i})', chave)
        
    escolha = input("Escolha: ")
    
    qtd_opcoes = len(opcoes)
    acertou = False
    escolha_int = None
    
    if escolha.isdigit():
        escolha_int = int(escolha)
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
                        
    print()
    if acertou:
        qtd_acertos += 1
        print("Acertou!")
    else:
        print("Errou!")
    print()

print(f"Você acertou {qtd_acertos} de {len(pergunta)+1} perguntas.")
