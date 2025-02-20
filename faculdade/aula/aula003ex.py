from random import randint

sorteado = randint(0,10)
tentativas = 0
escolha = -1
while escolha != sorteado:
    escolha = int(input("Escolha um numero: "))
    if escolha > sorteado:
        print('O numero sorteado é menor.')
    elif escolha < sorteado:
        print('O número sorteado é maior')
    tentativas+=1
print(f"Voce acertou em {tentativas} tentativas.")