# def linha(tam):
#     print('-'*tam)
# linha(50)


# def mostrar_nome(nome):
#     print(f'Boa noite {nome}')
# mostrar_nome('Thereza')

pessoas = []
while True:
    pessoa = input("Digite um nome: ")
    if pessoa == 'QUERO SAIR FILHA DA PUTA':
        print('Saindo...')
        break
    pessoas.append(pessoa)
print(pessoas)
    