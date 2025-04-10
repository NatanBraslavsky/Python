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



