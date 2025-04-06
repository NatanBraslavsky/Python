def zipper(list1, list2):
    indice_maximo = min(len(list1), len(list2))
    return [
        (list1[i], list2[i]) for i in range(indice_maximo)
    ]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP','MG', 'RJ']
print(zipper(l1, l2))   
