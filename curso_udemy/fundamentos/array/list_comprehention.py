
#?maneira comum de adicionar elementos na lista

# lista = []
# for i in range(10):
#     lista.append(i)

# print(lista)

#!usando list_comprehention
# lista = [i for i in range(10)]
# print(lista)

#!Mapeamento list_comprehention
# produtos = [
#     {'nome':'p1', 'preco': 20, },
#     {'nome':'p2', 'preco': 10, },
#     {'nome':'p3', 'preco': 30, },
# ]

# novos_produtos = [
#     {**produto, 'preco':produto['preco']*1.05}
#     if produto['preco']>20 else {**produto} 
#     for produto in produtos
# ]

# print(*novos_produtos, sep='\n')

#!filtro
lista = [n for n in range(10) if n % 2 == 0]
print(lista)