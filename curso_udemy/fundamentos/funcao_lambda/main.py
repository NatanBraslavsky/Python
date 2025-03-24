


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

# lista.sort(key=lambda item: item['nome'])
# for item in lista:
#     print(item)

#?Lambda serve para criar uma função 'rapida' que nao vamos ficar utilizando toda hora

# def soma(x,y):
#     return x+y
# print(soma(2,3))
# #!ao invés de fazer isso^, faça isso...

soma = lambda x, y : x+y
print(soma(2,3))




