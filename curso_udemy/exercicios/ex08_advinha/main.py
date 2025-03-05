palavra = 'montanha'
tentativas = 0
while True:
        tentativas+=1
        usuario_tentativa = input("Advinhe a frase: ").lower()            
        if usuario_tentativa == palavra:
            print(f"Voce acertou em {tentativas} tentativas.")
            break
        for i in range(len(usuario_tentativa)):
            if usuario_tentativa[i] == palavra[i]:
                print(f"{palavra[i]} ")
            else:
                print("* ")
                 
                
              

