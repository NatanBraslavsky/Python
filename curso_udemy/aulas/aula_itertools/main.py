from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator),sep='\n')

pessoas = [
     'João', 'Joana', 'Luiz', 'Letícia',
 ]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

#?Lógica para fazer a combinação
# lista = ["Joao", "Joana", "Jeferson", "Julia"]
# tamanho = len(lista)
# for i in range(tamanho):
#     for j in range(i+1, tamanho):
#         print(lista[i], lista[j])

print_iter((combinations(pessoas, 2)))
print()
print_iter((permutations(pessoas, 2)))
print()
print_iter((product(pessoas, camisetas)))
