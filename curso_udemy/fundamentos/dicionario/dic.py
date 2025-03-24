# pessoa = {## chave : valor
#     'nome' : 'natan',
#     'sobrenome' : 'braslavsky',
#     'idade' : '20',
#     'altura' : '1.90',
# }
# print(pessoa['nome'])
# ########################    

# for chave in pessoa:
#     print(chave, ':', pessoa[chave])
########################

# pessoa['rua'] = 'fagundes varela'
# print(pessoa['rua'])
########################

# if pessoa.get('sobrenome'):
#     print("existe")

########################
# print(pessoa.keys())#chave
# print(pessoa.values())#valores
# print(pessoa.items())#chave e valor
# for chave, valor in pessoa.items():
#     print(chave,':', valor)


########################

# pessoa.pop('sobrenome')
# print(pessoa)



########################

# pessoa.update({
#     'nome' : 'novo valor'
# })

# print(pessoa['nome'])

########################

# pessoa = {
#     'nome' : 'Luiza',
#     'sobrenome' : 'Souza',
# }

# (a1, b1), (a2, b2) = pessoa.items()
# print(a1, b1, a2, b2)


#########################

def mostro_argumenos_nomeados(**kwargs):
    print(kwargs)

mostro_argumenos_nomeados(nome= 'Joana', idade= 20)
