def binario(lista, certo):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        tent = lista[meio]
        if (tent == certo):
            return meio
        if (tent > certo):
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

lista = [1,3,5,7,9]
print(binario(lista, 3))