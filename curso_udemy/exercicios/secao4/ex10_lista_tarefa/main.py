from time import sleep
removido = []
tarefas = []
while True:
    try:
        sleep(0.5)
        escolha = int(input("\n1- Adicionar uma coisa a fazer\n2- Desfazer último hábito\n3- Refazer o que desfez\n4- Ver lista\n5- Sair\nEscolha: "))
        if escolha not in [1,2,3,4,5]:
            sleep(0.5)
            print("\nDigite um valor válido.")
        else:
            if escolha == 1:
                sleep(0.5)
                tare = input("\nDigite uma tarefa a fazer: ")
                tarefas.append(tare)
                sleep(0.5)
                print("Adicionado com sucesso.")
            elif escolha == 2:
                if len(tarefas) > 0:
                    removido.append(tarefas.pop())
                    sleep(0.5)
                    print(f"\nTarefa '{removido[len(removido)-1]}' removida com sucesso.")
                else:
                    sleep(0.5)
                    print("Lista vazia, impossível remover.")
            elif escolha == 3:
                try:
                    tarefas.append(removido[len(removido)-1])
                    print(f"\nTarefa '{removido[len(removido)-1]}' refeita com sucesso.")
                    removido.pop()
                    sleep(0.5)
                except:
                    sleep(0.5)
                    print("\nNenhuma tarefa foi removida para realizar essa ação.")
            elif escolha == 4:
                sleep(0.5)
                print(f"\nlista: {tarefas}")

            else:
                break
    except:
        print("\033[31mErro de digitação, Digite conforme o programa solicita.\033[0m")