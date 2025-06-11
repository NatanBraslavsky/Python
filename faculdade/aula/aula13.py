import tkinter as tk
from idlelib import tree
from tkinter import ttk,messagebox

root = tk.Tk()
root.geometry('500x500')
root.title('Exemplo de Treeview')
'''
colunas = ('Id','Nome','Email')
tree = ttk.Treeview(root,columns=colunas,show='headings')
tree.heading('Id',text='Id')
tree.column('Id',width=50)
tree.heading('Nome',text='Nome')
tree.column('Nome',width=150)
tree.heading('Email',text='Email')
tree.column('Email',width=150)

tree.insert('','end',values=(1,'Thereza','teste@gmail.com'))
tree.insert('','end',values=(2,'Gustavo','gustavo@gmail.com'))
tree.insert('','end',values=(3,'Fabiano','fabiano@gmail.com'))
tree.pack(fill=tk.BOTH,expand=1)
root.mainloop()'''

#Exemplo de treeview com crud --------------------------------------------

import tkinter as tk
from tkinter import ttk,messagebox

'''root = tk.Tk()
root.title('Exemplo Treeview')

colunas = ('ID','Nome','Email')
tree = ttk.Treeview(root,columns=colunas,show='headings')
tree.heading('ID',text='ID')
tree.column('ID',width=50)
tree.heading('Nome',text='Nome')
tree.column('Nome',width=150)
tree.heading('Email',text='Email')
tree.column('Email',width=150)

tree.insert('',tk.END,values=(1,'Maria','maria@gmail.com'))
tree.insert('',tk.END,values=(2,'Gustavo','gustavo@gmail.com'))
tree.insert('',tk.END,values=(3,'JP','jp@gmail.com'))
tree.pack(fill=tk.BOTH,expand=True) # Também é importante empacotar o widget na janela


root.mainloop()'''

import mysql.connector
from mysql.connector import errorcode

def criar_banco_tabela():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        if conexao.is_connected():
            print('Conexao estabelecida com o banco!')
        cursor = conexao.cursor()

        cursor.execute('create database if not exists Cadastro')
        print('Banco de dados cadastro criado com sucesso!')

        cursor.execute('use Cadastro')

        cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa(
        id int auto_increment primary key,
        nome varchar(50),
        email varchar(80)
        )
        """)
        print('Tabela pessoa criada com sucesso!')
        cursor.close()
        conexao.close()
    except ValueError as erro:
        print(f'Erro ao conectar o banco :{erro}')
criar_banco_tabela()

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database = 'cadastro'
    )
def adicionar():
    nome = entry_nome.get()
    email = entry_email.get()
    if not nome or not email:
        messagebox.showwarning('Atenção', 'Todos os campos são obrigatórios')
        return
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('insert into pessoa(nome,email) values (%s,%s)',(nome,email))
    conexao.commit()
    conexao.close()
    carregar_dados()
    limpar_campos()

def carregar_dados():
    for item in tree.get_children():
        tree.delete(item)
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('select * from pessoa')
    for row in cursor.fetchall():
        tree.insert('',tk.END,values=row)
    conexao.close()

def atualizar():
    item = tree.selection()
    if not item:
        messagebox.showwarning('Atenção','Selecione um item para atualizar')
        return
    id_pessoa=tree.item(item[0])['values'][0]
    nome=entry_nome.get()
    email=entry_email.get()
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('update pessoa set nome=%s,email=%s where id=%s',(nome,email,id_pessoa))
    conexao.commit()
    conexao.close()
    carregar_dados()
    limpar_campos()

def deletar():
    item = tree.selection()
    if not item:
        messagebox.showwarning('Atenção', 'Selecione um item para atualizar')
        return
    id_pessoa=tree.item(item[0])['values'][0]
    if messagebox.askyesno('Confirmação','Deseja realmente excluir este registro?'):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('delete from pessoa where id=%s',(id_pessoa,))
        conexao.commit()
        conexao.close()
        carregar_dados()
        limpar_campos()

def preencher_campos():
    item = tree.selection()
    if item:
        valores= tree.item(item[0])['values']
        entry.nome.delete(0,tk.END)
        entry.email.delete(0, tk.END)
        entry.nome.insert(0, valores[1])
        entry.email.insert(0, valores[2])

def limpar_campos():
    entry_nome.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    tree.selection_remove(tree.selection())

janela = tk.Tk()
janela.title('Sistema Crud com Treeview')
janela.geometry('500x500')

tk.Label(janela,text='Nome:').pack()
entry_nome = tk.Entry(janela,width=40)
entry_nome.pack()

tk.Label(janela,text='Email:').pack()
entry_email = tk.Entry(janela,width=40)
entry_email.pack()

frame_botoes = ttk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes,text='Adicionar',command=adicionar).grid(row=0,column=0,padx=5)
tk.Button(frame_botoes,text='Atualizar',command=atualizar).grid(row=0,column=1,padx=5)
tk.Button(frame_botoes,text='Deletar',command=deletar).grid(row=0,column=2,padx=5)

colunas = ('ID','Nome','Email')
tree = ttk.Treeview(janela,columns=colunas,show='headings')
for col in colunas:
    tree.heading(col,text=col)
    tree.column(col,width=150)
tree.pack(fill=tk.BOTH,expand=True,padx=10, pady=10)
tree.bind('<<TreeviewSelect>>',preencher_campos)

carregar_dados()
janela.mainloop()
