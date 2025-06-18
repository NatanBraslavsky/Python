def singleNumber(lista):
    for i in lista:
        if lista.count(i) == 1:
            return i
    return None

lista = [1,1,2,2,4,5]
print(singleNumber(lista))

dados = (3, 10.5, 'natan', True)
print(f"1: {dados[1]}, 2: {dados[3]}")
try:
    dados[0] = dados[2]
except:
    print("Não é possivel modificar os valores de uma tupla.")