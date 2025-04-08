x = [1,2,3,4]
novo_x = [i for i in x if i % 2 == 0]
print(novo_x)

#?porem tem o filter
novo = list(filter(lambda x:x%2==0, x))
print(novo)


def print_iter(iter):
    print(*list(iter), sep='\n')

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novo_produto = [p for p in produtos if p['preco'] > 11]
#ou
novo_produto = filter(lambda x: x['preco'] > 11, produtos)
print_iter(novo_produto)