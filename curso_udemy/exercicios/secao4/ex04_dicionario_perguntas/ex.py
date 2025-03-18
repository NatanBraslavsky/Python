from time import sleep

perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5x5?',
        'Opções' : ['25', '5', '45', '50'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['3', '2', '5', '4'],
        'Resposta' : '5',
    }
]

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    for i, opcoes in enumerate(pergunta['Opções']):
        print(f'{i})', opcoes)
    print()
    escolha = input("Escolha uma opção: ")
            
    
    print()