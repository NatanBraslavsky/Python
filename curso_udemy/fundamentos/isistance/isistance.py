lista = [1,2, 'a', True, [1,2], {1,3,4}, {'nome': 'luiz'}]

for item in lista:
    
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item.upper(),isinstance(item,str))
