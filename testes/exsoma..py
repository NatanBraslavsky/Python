
def soma(num):
    strnum = str(num)
    soma = 0

    for i in strnum:
        soma+=int(i)

    return soma

print(soma(321))