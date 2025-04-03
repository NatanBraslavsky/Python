from tkinter import *

produtos = {'feijao':56,
            'arroz':35,
            'peixe':71,
            }

def inserirExibir():
    nome = nome_entry.get()
    if nome in produtos:
        result_label.config(text= f'Produto existente: R${produtos[nome]}')
    elif nome == 'sair':
        tk.destroy()
    else:
        def adicionarProduto():
            preco = float(preco_entry.get())
            produtos[nome] = preco
            result_label.config(text='Cadastrado.')
            preco_entry.destroy()
            preco_btn.destroy()
            preco_label.destroy()
        result_label.config(text='')

        preco_label = Label(tk,text='Digite o preço do produto: ')
        preco_label.grid(row=3,column=0,padx=5,pady=5)

        preco_entry = Entry(tk)
        preco_entry.grid(row=4,column=0, padx=5,pady=5)
        
        preco_btn = Button(tk, text='Adicionar', command=adicionarProduto)
        preco_btn.grid(row=5,column=0, padx=5,pady=5)
        
        
            
tk = Tk()
tk.geometry('300x300')

nome_label = Label(tk,text='Digite o nome do produto: ')
nome_label.grid(row=0,column=0,padx=5,pady=5)

nome_entry = Entry(tk)
nome_entry.grid(row=1, column=0, padx=5,pady=5)

btnNome = Button(tk,text='Enviar', command=inserirExibir)
btnNome.grid(row=2,column=0,padx=5,pady=5)

result_label = Label(tk)
result_label.grid(row=6,column=0,padx=10,pady=10)

tk.mainloop()