def soma(x, y):
    return x+y

soma = soma(1,2)
print(soma)

def soma_args(*args):#recebe todos os valores passados como parametro fora da função
    soma = sum(args)
    return soma
tupla = (1,2,3,4,5)
print(soma_args(*tupla))#desempacotei a tupla... pode ser um array também
