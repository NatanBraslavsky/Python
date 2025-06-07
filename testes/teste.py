
# soma = lambda x,y : x+y
# print(soma(5,3))


# def soma(x,y):
#     return x+y
# print(soma(5,3))


# num = [1,2,3,4,2,3,3,2,3,]
# num2 = set(num)
# print(num)
# print(num2)


# def isPar(num):
#     if num % 2 == 0:
#         return 'Par'
#     return 'Ímpar'

# print(isPar(2))

# def soma_lista(lista):
#     soma = sum(lista)
#     return soma

# print(soma_lista([1,2,3]))

# def soma_algoritimo_sum(lista):
#     soma = 0
#     for i in lista:
#         soma+=i
#     return soma

# def adicionar(pessoas):
#     try: 
#         nome = input("Digite o nome: ")
#         idade = int(input("Digite sua idade: "))
#         pessoas[nome] = idade
#     except:
#         print("Digite algo válido.")

# def listar(pessoas):
#     for chave, valor in pessoas.items():
#         print(f"{chave}:{valor}")

# def atualizar(pessoas):
#     nom = input("Digite o nome da pessoa: ")
#     if nom in pessoas:
#         ida = int(input("Idade: "))
#         pessoas[nom] = ida
#     else:
#         print("Nome nao encontrado.")

# def remover(pessoas):
#     nom = input("Digite o nome da pessoa: ")
#     del pessoas[nom]

# def sair():
#     exit()

# pessoas = {

# }
# while True:
#     escolha = input(
#         "1- Adicionar pessoa.\n"
#         "2- Listar pessoas.\n"
#         "3- Atualizar idade de uma pessoa.\n"
#         "4- Remover uma pessoa\n"
#         "5- Sair"
#     )

#     comando = {
#         "1": lambda: adicionar(pessoas),
#         "2": lambda: listar(pessoas),
#         "3": lambda: atualizar(pessoas),
#         "4": lambda: remover(pessoas),
#         "5": lambda: sair(),
#     }

#     if escolha in comando:
#         comando[escolha]()
#     else:
#         print("Digite um valor válido.")

# x1 = []
# for i in range(5):
#     a = int(input("Digite um valor: "))
#     x1.append(a)

# b = set(x1)
# print(b)


# soma = lambda x,y : x+y
# print(soma(5,3))


# def soma(x,y):
#     return x+y
# print(soma(5,3))

# def isPar(num):
#     if num % 2 == 0:
#         return 'Par'
#     return 'Ímpar'

# print(isPar(2))


soma = lambda x,y : x+y
print(soma(5,3))


def soma(x,y):
    return x+y
print(soma(5,3))

def isPar(num):
    if num % 2 == 0:
        return 'Par'
    return 'Ímpar'

print(isPar(2))
