nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
tamanho = len(nome)

if not nome or not idade:
    print('Desculpe, você deixou campos vazios.')
else:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[-1: -tamanho: -1]}")
print(2)