
#?ex001
# numInput = input("Digite um número: ")
# num = float(numInput)
# if num > 0:
#     print("Seu número é positivo.")
# elif num < 0:
#     print("Seu número é negativo.")
# else:
#     print("Seu numero é zero.")

#?ex002
# notas = []
# soma = 0
# for i in range(3):
#     nota = float(input(f"Digite a {i+1} nota: "))
#     notas.append(nota)
#     soma += notas[i]
# media = soma / 3
# print("Media: ", media)
# if media >= 7:
#     print("Aprovado.")
# elif media < 5:
#     print("Reprovado.")
# else:
#     print("Recuperação.")

#?ex003
# numeros = []
# for i in range(2):
#     if i == 0:
#         num = float(input("Digite um número: "))
#     else:
#         num = float(input("Digite outro número: "))
#     numeros.append(num)
# if numeros[0] % numeros[1] == 0:
#     print("Sim.")
# else:
#     print("Não.")

#?ex004
# numeros = []
# maior = 0
# menor = 0
# for i in range(3):
#     num = int(input("Digite um número: "))
#     numeros.append(num)
#     if numeros[i] > maior:
#         maior = numeros[i]
#     if numeros[i] < menor or i == 0:
#         menor = numeros[i]

# if numeros[0] == menor and numeros[2] == maior:
#     print("Estão ordenados corretamente.")
# else:
#     print("Não estão ordenados corretamente.")

#?ex005
# num = int(input("Digite um número inteiro: "))
# qtdimpar = 0
# for i in range(1, num + 1, 2):
#     qtdimpar+=1
# print(qtdimpar)

#?ex006
# def fatorial(num):
#     fat = 1
#     for i in range(num, 1, -1):
#         fat*=i
#     return fat    

# num = int(input("Digite um número: "))
# print(f"{fatorial(num)}")
  
#?ex007
# num = input("Digite um número inteiro: ")  
# print(f"O número digitado tem {len(num)} dígitos.")

#?ex008
# def perfeito(num):
#     divisiveis = []
#     for i in range(num - 1, 0, -1):
#         if num % i == 0:
#             divisiveis.append(i)

#     soma = 0
#     for i in divisiveis:
#         soma += i
#     if soma == num:
#         return True
#     else:
#         return False

# numero = int(input("Digite um número: "))
# if (perfeito(numero)):
#     print("Número perfeito.")
# else:
#     print("Não número perfeito.")

#?ex009
# def fibonacci(num):
#     fib = [0, 1]
#     for i in range(2, num + 1):
#         fib.append(fib[i - 1] + fib[i - 2]) 
#     return fib[:num] 

# num = int(input("Digite um numero: "))
# print(fibonacci(num))

#?ex010
def tabuada(base, limite):
    for i in range(1, limite+1):
        print(f"{base} * {i} = {base*i}")


base = int(input("Digite o numero base: "))
limite = int(input("Digite o numero limite: "))
tabuada(base, limite)

