
def singleNumber(lista):
    for i in lista:
        if lista.count(i) == 1:
            return i
    return None

lista = [1,1,2,2,4,5]
print(singleNumber(lista))