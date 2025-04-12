# def soma(x, y):
#     return x+y

# soma = soma(1,2)
# print(soma)

# def soma_args(*args):#recebe todos os valores passados como parametro fora da função
#     soma = sum(args)
#     return soma
# tupla = (1,2,3,4,5)
# print(soma_args(*tupla))#desempacotei a tupla... pode ser um array também


def adicionarLista(nome, lista = None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes1 = adicionarLista("Daniel")
adicionarLista("Davi", clientes1)
adicionarLista("Natan", clientes1)

clientes2 = adicionarLista("Fabio")
adicionarLista("Tatiana", clientes2)

print(f"C1 = {clientes1}\nC2 = {clientes2}")