import random

frase = 'Olá natan como vai'.lower().replace(' ', '')

mais_vezes = 0
letra_apareceu_mais = ''
for i in range(len(frase)):
    letra = frase[i]
    qtd_letra = frase.count(letra)
    if mais_vezes < qtd_letra:
        mais_vezes = qtd_letra
        letra_apareceu_mais = letra
    
print(f"Letra que apareceu mais vezes: {letra_apareceu_mais}")

