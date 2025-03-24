


lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#?Função para ordenar um dicionario: 
# def ordenar(item):
#     return item['nome']


# lista.sort(key=ordenar) #!passo o nome da função

# for item in lista:
#     print(item)

#*Porém tem outra maneiro com a função lambda:

lista.sort(key=lambda item: item['nome'])
for item in lista:
    print(item)

