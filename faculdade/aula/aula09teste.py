from mysql import connector
import mysql
from tkinter import *
import tkinter.messagebox as MessageBox

connection = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Senha123@',
    database = ''
)

cursor = connection.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS loja')
cursor.execute('USE loja')

cursor.execute('''CREATE TABLE IF NOT EXISTS produto(
                codigo INT PRIMARY KEY,
                nome VARCHAR(20) NOT NULL,
                preco DECIMAL(10,2) NOT NULL,
                quantidade INT NOT NULL
                )''')

tk = Tk()
tk.geometry('500x300')
tk.title('loja')

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()
    
    if codigo == '' or nome == '' or preco == '' or quantidade == '':
        MessageBox.showerror('Inserir', 'Todos os campos são obrigatórios')
    else:
        cursor.execute('INSERT INTO produto(codigo,nome,preco,quantidade) VALUES (%s,%s,%s,%s)',(codigo,nome,preco,quantidade))
        connection.commit()
        MessageBox.showinfo('Inserir', 'Produto inserido com sucesso!')

        e_codigo.delete(0,END)
        e_nome.delete(0, END)
        e_preco.delete(0, END)
        e_quantidade.delete(0, END)

def excluir():
    codigo = e_codigo.get()
    if codigo == '':
        MessageBox.showerror('Excluir', 'Informe o código do produto')
    else:
        cursor.execute('DELETE FROM produto WHERE codigo = %s', (codigo,))
        connection.commit()
        if cursor.rowcount == 0:
            MessageBox.showerror('Excluir', f'Nenhum produto com código {codigo} foi encontrado.')
        else:
            MessageBox.showinfo('Excluir', 'Produto excluído com sucesso!')
        e_codigo.delete(0, END)


Label(tk, text='Código').place(x=20,y=30)
Label(tk, text='Nome').place(x=20,y=60)
Label(tk, text='Preço').place(x=20,y=90)
Label(tk, text='Quantidade').place(x=20,y=120)

e_codigo = Entry(tk)
e_codigo.place(x=100, y=30) 

e_nome = Entry(tk)
e_nome.place(x=100, y=60)

e_preco = Entry(tk)
e_preco.place(x=100, y=90)

e_quantidade = Entry(tk)
e_quantidade.place(x=100, y=120)

Button(tk, text='Inserir', command=inserir).place(x=30, y=160)
Button(tk, text='Excluir', command=excluir).place(x=80, y=160)



tk.mainloop()