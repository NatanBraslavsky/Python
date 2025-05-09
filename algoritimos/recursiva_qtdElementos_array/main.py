def contar_elementos(arr):
    if arr == []:
        return 0
    else:
        return 1 + contar_elementos(arr[1:])
    
print(contar_elementos([1,5,3]))