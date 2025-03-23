
#!1
# numExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezessete", "dezoito", "dezenove", "vinte")

# escolha = int(input("Digite um numero entre 0 e vinte: "))
# print(numExtenso[escolha])

#!2
# listaNum = []
# for i in range(10):
#     num = int(input("Digite um número: "))
#     listaNum.append(num)

# numeros_unicos = []

# for num in listaNum:
#     if num not in numeros_unicos:  
#         numeros_unicos.append(num)

# qtdDiferente = len(numeros_unicos)

# print(f"Quantidade de números diferentes: {qtdDiferente}")

#!3
# valores = []
# for i in range(3):
#     valores.append(int(input("Digite um valor: ")))

# qtdNove = valores.count(9)
# indexTres = valores.index(3) if 3 in valores else -1
# numPar = [num for num in valores if num % 2 == 0]

# print(f"Quantidade 9: {qtdNove}")
# if indexTres != -1:
#     print(f"Num 3 na posição: {indexTres}")
# else:
#     print("Numero 3 nao está na lista.")
# print(f"Numeros pares: {numPar}")

#!4
# from random import randint
# qtdSeis = 0
# for i in range(50):
#     lancado = randint(1,6)
#     if lancado == 6:
#         qtdSeis += 1
# probabilidade = (qtdSeis / 50) * 100
# print(f"O número seis caiu: {probabilidade:.2f}% das vezes.")

#!5
# traducao = {
#     "porta" : "door",
#     "teclado" : "keyboard",
#     "fazer" : "make",
#     "limpar" : "clean",
#     "lixo" : "thresh",
#     "estudar" : "study",
# }

# palavra = input("Digite uma palavra para saber a tradução: ")
# if palavra not in traducao.keys():
#     print("Palavra não encontrada no dicionario.")
# else:
#     print(f"Tradução: {traducao[palavra]}") 

#!6
# from time import sleep
# produtos = {

# }
# while True:
#     escolha = int(input("\nSelecione uma opção:\n\n1-Cadastrar Produto\n2-Ver Produto\n3-Sair\nEscolha: "))
#     print()

#     if escolha == 1:
#         sleep(1)
#         nomeProduto = input("Nome Produto: ")
#         qtdProduto = input("Quantidade Produto: ")
#         produtos[nomeProduto] = qtdProduto
#         print("Cadastro concluido.")
#         print("-"*20)
#         sleep(1)

#     elif escolha == 2:
#         sleep(1)
#         print("Produtos: ")
#         for chave, valor in produtos.items():
#             print(f"Nome : {chave} | Quantidade : {valor}")
#         sleep(1)
    
#     elif escolha == 3:
#         sleep(1)
#         print("Saindo...")
#         break
    
#     else:
#         sleep(1)
#         print("Valor inválido.")

#!7
# idades = []
# alturas = []
# for i in range(5):
#     idades.append(int(input("Idade: ")))
#     alturas.append(float(input("Altura: ")))

# for i in range(4, 0, -1):
#     print(f"idade: {idades[i]}, altura: {alturas[i]}")

#!8
# alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# palavra = input("Digite uma palavra: ")
# ocorrencias = {

# }
# for letra in alfabeto:
#     qtdLetra = palavra.count(letra)
#     ocorrencias[letra] = qtdLetra

# for chave, valor in ocorrencias.items():
#     print(f"{chave} : {valor}")

#!9
# def mediaAluno(**args):
#     alunoMedia = {}
#     for i, v in args.items():
#         soma = sum(v)
#         media = soma / 3
#         mediaFormatada = f"{media:.2f}"
#         alunoMedia[i] = mediaFormatada

#     return alunoMedia


# aluno = {
#     "joao" : (7.5, 5.8, 8.2),
#     "davi" : (3.5, 4.8, 7.2),
#     "natan" : (9.5, 8.4, 10),
# }
# print(f"{mediaAluno(**aluno)}")

#!10
# ocorrenciaPalavra = {}
# string = input("Digite uma string: ")
# listaPalavras = string.split(" ")
# for i in listaPalavras:
#     ocorrenciaPalavra[i] = listaPalavras.count(i)
# print(ocorrenciaPalavra)
    
#!11
# def positivoNegativo(n):
#     posNeg = "Positivo" if n > 0 else "Negativo"
#     print(posNeg)

# while True:
#     num = int(input("Digite um número: "))
#     if num != 0:
#         positivoNegativo(num)
#         break
#     else:
#         print("Numero inválido")

#!12
# def valorAbsoluto(n):
#     print(abs(n))

# valorAbsoluto(+5)

#!13
# def somaLimite(a,b,limite):
#     return True if a+b <= limite else False

# print(somaLimite(2,9,10))

#!14
# def somaImposto(taxaImposto, custo):

#     imposto = custo * (taxaImposto / 100)

#     return custo + imposto

# taxaImposto = 20  
# custo = 100  

# custoComImposto = somaImposto(taxaImposto, custo)
# print(f"O custo com o imposto é: R${custoComImposto:.2f}")

#!15
def qtdDigitos(num):
    print(len(str(num)))

qtdDigitos(545)
