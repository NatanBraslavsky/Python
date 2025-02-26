from time import sleep

while True:
    try:
        num1 = float(input("Digite um número: "))
        break
    except:
        sleep(0.5)
        print("\nErro. Tente novamente.\n")
        sleep(0.5)
while True:
    try:
        num2 = float(input("Digite outro número: "))
        break
    except:
        sleep(0.5)
        print("\nErro. Tente novamente.\n")
        sleep(0.5)
while True:
    try:
        operacao = int(input("1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\nDigite a operação: "))
        if operacao in [1,2,3,4]:
            if operacao == 1:
                print(f"{num1} + {num2} = {num1+num2}")
            elif operacao == 2:
                print(f"{num1} + {num2} = {num1+num2}")
            elif operacao == 3:
                print(f"{num1} + {num2} = {num1+num2}")
            elif operacao == 4:
                print(f"{num1} + {num2} = {num1+num2}")
            break
        else:
            sleep(0.5)
            print("\nErro. Tente novamente.\n")
            sleep(0.5)
    except:
        sleep(0.5)
        print("\nErro. Tente novamente.\n")
        sleep(0.5)