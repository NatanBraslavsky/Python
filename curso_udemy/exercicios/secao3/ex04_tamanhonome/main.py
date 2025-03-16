nome = input("Digite seu nome: ")
tamanho = len(nome)
if tamanho <= 4:
    print("Nome curto.")
elif 4 < tamanho <= 6:
    print("Nome normal.")
else:
    print("Seu nome é muito grande")