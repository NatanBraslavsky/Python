def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadriplicar = criar_multiplicar(4)
print(duplicar(2))
print(triplicar(3))
print(quadriplicar(4))