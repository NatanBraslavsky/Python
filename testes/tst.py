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



def contar_elementos(arr):
    if arr == []:
        return 0
    else:
        return 1 + contar_elementos(arr[1:])
    
print(contar_elementos([1,5,3]))


from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1 , 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))