from random import randint

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menor = [i for i in arr[1:] if i <= pivo]
        maior = [i for i in arr[1:] if i > pivo]
        return quicksort(menor) + [pivo] + quicksort(maior)
print(quicksort([5,4,3,3,5,3,1]))



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