
num = input("Digite um número: ")
try:
    numero = int(num)
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar.")
except:
    print("Isso não é um número inteiro.")

if(len(num) < 3):
    print("menor que 3")