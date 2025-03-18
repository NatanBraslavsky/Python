pessoa = {
    'nome' : 'natan',
    'sobrenome' : 'braslavsky',
    'idade' : '20',
    'altura' : '1.90',
}
print(pessoa['nome'])
########################

for chave in pessoa:
    print(chave, ':', pessoa[chave])
########################

pessoa['rua'] = 'fagundes varela'
print(pessoa['rua'])
########################

if pessoa.get('sobrenome'):
    print("existe")

########################
print(pessoa.keys())#chave
print(pessoa.values())#valores
print(pessoa.items())#chave e valor
for chave, valor in pessoa.items():
    print(chave,':', valor)