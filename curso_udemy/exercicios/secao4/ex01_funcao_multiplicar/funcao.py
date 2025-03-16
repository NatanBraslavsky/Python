def multiplicacao(*args):
    mult = 1
    for i in args:
        mult *= i

    return mult

multiplicacao = multiplicacao(1,2,3,4,5)
print(multiplicacao)