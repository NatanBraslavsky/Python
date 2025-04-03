from tkinter import *

produtos = {'feijao':56,
            'arroz':35,
            'peixe':71,
            }

def inserirExibir():
    nome = nome_entry.get()
    if nome in produtos:
        result_label.config(text=produtos.values())
    if nome == 'sair':
        tk.destroy()
    else:
        def adicionarProduto():
            preco = float(preco_entry.get())
            produtos[nome] = preco
            result_label.config(text='Cadastrado.')
            
        preco_entry = Entry(tk)
        preco_entry.grid(row=3,column=0)
        
        preco_btn = Button(tk, text='Adicionar', command=adicionarProduto)
        preco_btn.grid(row=4,column=0)
        
        
            
tk = Tk()
tk.geometry('300x300')

nome_entry = Entry(tk)
nome_entry.grid(row=0, column=0, padx=5,pady=5)

btnNome = Button(tk,text='Enviar', command=inserirExibir)
btnNome.grid(row=2,column=0,padx=5,pady=5)

result_label = Label(tk)
result_label.grid(row=5,column=0,padx=10,pady=10)

tk.mainloop()