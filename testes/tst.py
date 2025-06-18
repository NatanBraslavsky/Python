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