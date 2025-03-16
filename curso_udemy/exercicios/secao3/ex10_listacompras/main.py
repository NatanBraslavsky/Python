import os

lista = []

while True:
    escolha = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ').lower()
    if escolha == 'i':
        os.system('cls')
        inserir = input("Digite um valor: ")
        lista.append(inserir)
    elif escolha == 'a':
        remover = input("Escoha um indice para remover da lista: ")
        try:
            indice = int(remover)
            del lista[indice]
        except ValueError:
            print("Digite um número int.")
        except IndexError:
            print("Índice não existe na ista.")
        except Exception:
            print("Erro desconhecido")
    elif escolha == 'l':
        os.system('cls')
        if len(lista) == 0:
            print("Lista vazia.")
        for indice, nome in enumerate(lista):
            print(indice, nome)
    else:
        print('Digite um valor válido.')