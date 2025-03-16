import time

while True:
    try:
        escolha = int(input("1- Entrar\n2- Sair\n3- Cadastrar\nOpcao:"))
        if escolha in [1,2,3]:
            print("Entrou")
            time.sleep(1)
            print("Finalizando...")
            break
        else:
            print("Escolha uma opção válida.\n")
            time.sleep(1)
    except:
        print("ERRO.")
