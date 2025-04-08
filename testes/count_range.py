lista = ["Joao", "Joana", "Jeferson", "Julia"]
tamanho = len(lista)
for i in range(tamanho):
    for j in range(i+1, tamanho):
        print(lista[i], lista[j])