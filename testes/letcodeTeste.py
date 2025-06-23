# def listaOrdenada(list1,list2):
#     list3 = list1+list2
#     ordList3 = sorted(list3)
#     return ordList3

# list1 = []
# list2 = []
# print(listaOrdenada(list1,list2))

def somaUltimo(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits

digitos = [1,2,3,4,5,6,7]
print(somaUltimo(digitos))



def goodpar(nums):
    qtdGoodPar = 0
    tamanhoArray = len(nums)
    for i in range(tamanhoArray):
        for j in range(i+1,tamanhoArray):
            if nums[i] == nums[j]:
                qtdGoodPar+=1
    return qtdGoodPar

arr = [1,2,3]
print(goodpar(arr))