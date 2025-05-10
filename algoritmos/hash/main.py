vot = {}
def verificarVoto(nome):
    if vot.get(nome):
        print("Mande embora.")
    else:
        vot[nome] = True
        print("Deixe votar.")
verificarVoto("tom")
verificarVoto("alice")
verificarVoto("alice")