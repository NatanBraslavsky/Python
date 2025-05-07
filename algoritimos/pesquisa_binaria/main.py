def binaria(lista, certo):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == certo:
            return meio
        if chute > certo:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

lista = [1,3,5,7,9]
print(binaria(lista,3))