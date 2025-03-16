nome = 'Luiz Otávio'
contador = 0
novo = ''
while contador < len(nome):
    novo += f'*{nome[contador]}*'
    contador+=1
print(novo)