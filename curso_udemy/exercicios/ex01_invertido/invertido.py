nome = input('Digite seu nome: ')
idade_input = input('Digite sua idade: ')

if not nome or not idade_input.isdigit():
    print('Desculpe, você deixou campos vazios.')
else:
    idade = int(idade_input)
    tamanho = len(nome)
    qtdCaracteres = len(nome.replace(" ", ""))
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[-1 : - tamanho - 1: - 1]}")  
    if ' ' in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome nao contém espaços.")
    print(f"Quantidade de letras: {qtdCaracteres}")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")
    
    
