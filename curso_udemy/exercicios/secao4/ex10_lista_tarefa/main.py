from time import sleep
import escolhas

removido = []
tarefas = []

while True:
    try:
        sleep(0.5)
        escolha = input(
            "\n1- Adicionar uma coisa a fazer\n"
            "2- Desfazer último hábito\n"
            "3- Refazer o que desfez\n"
            "4- Ver lista\n"
            "5- Sair\n"
            "Escolha: "
        )

        comando = {
            '1': lambda: escolhas.adicionar(tarefas),
            '2': lambda: escolhas.desfazer(tarefas, removido),
            '3': lambda: escolhas.refazer(tarefas, removido),
            '4': lambda: print(f"\nLista: {tarefas}"),
            '5': lambda: escolhas.exit_programa(),
        }

        if escolha in comando:
            comando[escolha]()
        else:
            print("\n\033[31mDigite uma opção válida.\033[0m")

    except Exception as e:
        print("\033[31mErro de digitação, digite conforme o programa solicita.\033[0m")