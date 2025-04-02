import copy

from packageProdutos import produtos

#?aumentar o preco em 10%
novoProduto = [
    {**p, 'preco':round(p['preco']*1.1,2)} for p in copy.deepcopy(produtos)
]

print(*novoProduto, sep='\n')


#?ordenado por nome decrescente
print('\n')
produto_ordenado_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse=True
    )

print(*produto_ordenado_por_nome, sep='\n')


#?ordenado por preco
print('\n')
produto_ordenado_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['preco']
)

print(*produto_ordenado_por_preco, sep='\n')