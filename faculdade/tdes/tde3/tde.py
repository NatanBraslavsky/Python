
#ex 1
# dados = (3, 10.5, 'natan', True)
# print(f"1: {dados[1]}, 2: {dados[3]}")
# try:
#     dados[0] = dados[2]
# except:
#     print("Não é possivel modificar os valores de uma tupla.")
    
#ex 2
# tupla = (1,2,2,3,2)
# print(tupla.count(2))


#ex 3
# numeros = [1,2,3,4,5]
# numeros.append(100)
# del numeros[2]
# numeros[0] = 500
# print(numeros)


#ex 4
# soma = 0
# notas = [5.5, 7.4, 8.9, 10, 5.2]
# for i in notas:
#     soma += i
# media = soma / 5
# print(media)


#ex 5
# numeros = [5,3,6,8,2,1]
# numeros.sort()
# print(numeros)
# numeros.sort(reverse= True)
# print(numeros)
# for i in numeros:
#    if i > 10:
#         print(i)
    

#ex 6
# notas = [[7, 8, 9, 6], [6, 5, 8, 7], [10, 9, 8, 9]]
# print(notas[1][2])
# soma = [0, 0, 0]
# media = [0, 0, 0]
# for i in range(3):
#     for j in range(4):
#         soma[i] += notas[i][j]
# for i in range(3):
#     media[i] = soma[i] / 4
# print(max(media))
# Calcule a média de cada aluno e imprima o nome do aluno com a maior
# média.


#ex 7 
# vetor = []
# indextres = 0
# for i in range(4):
#     vetor.append(float(input("Digite um valor")))
#     if vetor[i] == 3:
#         indextres = i
#     if vetor[i] % 2 == 0:
#         print(vetor[i])
    
# print(f"9: {vetor.count(9)}")
# print(f"O número tres foi digitado no index {indextres}")


#ex 8
from random import randint
lista = [0] * 50
for i in range(50):
    lista[i] = randint(1, 6)

porcentagem = lista.count(6) 
print(f"{porcentagem}/50")
porcent = (porcentagem / 50) * 100
print(porcent)



