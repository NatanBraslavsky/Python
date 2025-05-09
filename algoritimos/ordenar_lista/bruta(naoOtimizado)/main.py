def acharMenor(lista):
    menor = lista[0]
    indiceMenor = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indiceMenor = i
    return indiceMenor

def ordenarLista(lista):
    novaLista = []
    for i in range(len(lista)):
        menor = acharMenor(lista)
        novaLista.append(lista.pop(menor))
    return novaLista

print(ordenarLista([3,5,1,2]))