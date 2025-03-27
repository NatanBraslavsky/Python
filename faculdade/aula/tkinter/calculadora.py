import tkinter as tk

# Função para adicionar números e operações na tela
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Função para calcular o resultado
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

# Função para apagar a tela
def clear():
    entry.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Campo de entrada (onde o usuário digita os números e operações)
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Criando os botões e associando as funções
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Iniciar a interface gráfica
root.mainloop()
