import json
 
# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

#?criando o arquivo json
# with open('.\\curso_udemy\\aulas\\aula_json\\aulajson.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa,arquivo)



#?acessando o arquivo json
with open('C:\\Users\\natan\\OneDrive\\Documentos\\Estudos\\python\\curso_udemy\\aulas\\aula_json\\aulajson.json', 'r') as arquivo:
    pessoa = json.load(arquivo)

for chave, valor in pessoa.items():
    print(chave, valor)