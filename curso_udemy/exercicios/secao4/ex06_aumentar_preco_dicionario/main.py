produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
 ]

newProduto = [
    {**produto, 'preco':produto['preco']*1.10} for  produto in produtos
]

for i in newProduto:
    for chave,valor in i.items():
        print(chave, valor)
