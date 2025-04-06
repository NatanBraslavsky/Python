def soma(l1,l2):
    maximo = min(len(l1), len(l2))
    return [l1[i]+l2[i] for i in range(maximo)]

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4]
print(soma(l1,l2))

#?ou

listaSoma = [x+y for x,y in zip(l1,l2)]
print(listaSoma)


