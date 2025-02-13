import time

while True:
    print("\nEscolha a operação matemática:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = int(input("Escolha a operação: "))

    if escolha in [1, 2, 3, 4]:
        break
    else:
        time.sleep(1)
        print("Escolha inválida, tente novamente.")
        time.sleep(1)

while True:
    num1 = int(input("Digite um valor inteiro: "))
    if num1 > 0:
        break  
    else:
        time.sleep(1)
        print("Digite um número maior que 0.")
        time.sleep(1)

while True:
    num2 = int(input("Digite outro valor inteiro: "))
    if num2 > 0:
        break
    else:
        time.sleep(1)
        print("Digite um número maior que 0.")
        time.sleep(1)

if escolha == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif escolha == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif escolha == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
else:
    if num2 == 0:
        print("Erro: Não é possível dividir por zero.")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
