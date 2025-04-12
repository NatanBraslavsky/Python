from time import sleep

def adicionar(tarefas):
    sleep(0.5)
    tare = input("\nDigite uma tarefa a fazer: ")
    tarefas.append(tare)
    sleep(0.5)
    print("Adicionado com sucesso.")

def desfazer(tarefas, removido):
    if len(tarefas) > 0:
        removido.append(tarefas.pop())
        sleep(0.5)
        print(f"\nTarefa '{removido[len(removido)-1]}' removida com sucesso.")
    else:
        sleep(0.5)
        print("Lista vazia, impossível remover.")

def refazer(tarefas, removido):
    try:
        tarefas.append(removido[len(removido)-1])
        print(f"\nTarefa '{removido[len(removido)-1]}' refeita com sucesso.")
        removido.pop()
        sleep(0.5)
    except:
        sleep(0.5)
        print("\nNenhuma tarefa foi removida para realizar essa ação.")

def exit_programa():
    sleep(0.5)
    print("Encerrando programa...")
    sleep(0.3)
    exit()

