# lista = []

# try:
#     with open("arquivo.json", "r") as arquivo:
#         for linha in arquivo:
#             lista.append(linha)
# except:
#     pass

# while True:
#     num = int(input("Digite um valor(0 para sair): "))
#     if num == 0:
#         break
#     if num in lista:
#         print("Valor ja na lista.") 
#     else:
#         lista.append(num)
#         with open("arquivo.json", "a") as arquivo:
#             arquivo.write(f"{num}\n")


    
lista = []
try:
    with open("jsonfile.json", "r") as arquivo:
        for linha in arquivo:
            lista.append(linha)
except:
    pass

while True:
    num = int(input("Digite um número(0 para sair.): "))
    if num == 0:
        break
    if num in lista:
        print("Número já na lista.")
    else:
        lista.append(num)
        with open("jsonfile.json", "a") as arquivo:
            arquivo.write(f"{num}\n")
