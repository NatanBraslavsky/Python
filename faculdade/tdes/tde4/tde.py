
#!1
# numExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezessete", "dezoito", "dezenove", "vinte")

# escolha = int(input("Digite um numero entre 0 e vinte: "))
# print(numExtenso[escolha])

#!2
# listaNum = []
# for i in range(10):
#     num = int(input("Digite um número: "))
#     listaNum.append(num)

# numeros_unicos = []

# for num in listaNum:
#     if num not in numeros_unicos:  
#         numeros_unicos.append(num)

# qtdDiferente = len(numeros_unicos)

# print(f"Quantidade de números diferentes: {qtdDiferente}")

#!3
# valores = []
# for i in range(3):
#     valores.append(int(input("Digite um valor: ")))

# qtdNove = valores.count(9)
# indexTres = valores.index(3) if 3 in valores else -1
# numPar = [num for num in valores if num % 2 == 0]

# print(f"Quantidade 9: {qtdNove}")
# if indexTres != -1:
#     print(f"Num 3 na posição: {indexTres}")
# else:
#     print("Numero 3 nao está na lista.")
# print(f"Numeros pares: {numPar}")

#!4
# from random import randint
# qtdSeis = 0
# for i in range(50):
#     lancado = randint(1,6)
#     if lancado == 6:
#         qtdSeis += 1
# probabilidade = (qtdSeis / 50) * 100
# print(f"O número seis caiu: {probabilidade:.2f}% das vezes.")
