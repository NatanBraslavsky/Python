pessoas = [
    {'nome' : 'natan', 'idade' : 20},
    {'nome' : 'davi', 'idade' : 24},
    {'nome' : 'daniel', 'idade' : 27},
]

novo_produto = [
    {**pessoas} 
    for pessoas in pessoas
]

for produto in novo_produto:
    print(produto)