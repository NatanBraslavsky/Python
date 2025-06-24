import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'Senha123@',
    database = 'revisaoAV2'
)
cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS revisaoAV2')

# cursor.execute('USE revisaoAV2')

cursor.execute('''CREATE TABLE IF NOT EXISTS aluno(
                id_aluno INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(30),
                email VARCHAR(50),
                telefone INT,
                data_nascimento INT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS cursos(
                id_curso INT PRIMARY KEY AUTO_INCREMENT,
                nome_curso VARCHAR(20),
                descricao VARCHAR(30)            
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS matricula(
                id_matricula INT PRIMARY KEY AUTO_INCREMENT,
                data_matricula VARCHAR(10),
                id_aluno INT,
                FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
                id_curso INT,
                FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
)''')



root = Tk()
root.title('Teste')
root.geometry('500x500')

def adicionar():
    nomeAluno = entryNomeAluno.get()
    emailAluno = entryEmailAluno.get()
    telefoneAluno = entryTelefoneAluno.get()
    dataAluno = entryDataAluno.get()
    try:
        if nomeAluno == '' or emailAluno == '' or telefoneAluno == '' or dataAluno == '':
            MessageBox.showerror('Inserir', 'Todos os campos são obrigatórios')
        else:
            cursor.execute('INSERT INTO aluno(nome, email, telefone, data_nascimento) VALUES (%s, %s, %s, %s)',(nomeAluno, emailAluno, telefoneAluno, dataAluno))
            connection.commit()
            MessageBox.showinfo('Inserir', 'Aluno Cadastrado com sucesso.')
    except:
        MessageBox.showerror('Inserir', 'Erro de tipagem')

def atualizar():
    nomeAluno = entryNomeAluno.get()
    emailAluno = entryEmailAluno.get()
    telefoneAluno = entryTelefoneAluno.get()
    dataAluno = entryDataAluno.get()
    try:
        cursor.execute('UPDATE aluno SET nome=%s,email=%s,data_nascimento=%s WHERE telefone = %s', (nomeAluno, emailAluno, dataAluno, telefoneAluno))
        MessageBox.showinfo('Atualizar', 'Usuário atualizado com sucesso')
    except:
        MessageBox.showerror('Atualizar', 'Erro, Tente novamente')
labelAluno = Label(root, text='Aluno')
labelAluno.grid(row=0, column=1, padx=15, pady=15)

labelNomeAluno = Label(root, text='Nome')
labelNomeAluno.grid(row=1, column=0)

entryNomeAluno = Entry(root)
entryNomeAluno.grid(row=1, column=1)

labelEmailAluno = Label(root, text='Email')
labelEmailAluno.grid(row=2, column=0)

entryEmailAluno = Entry(root)
entryEmailAluno.grid(row=2, column=1)

labelTelefoneAluno = Label(root, text='Telefone')
labelTelefoneAluno.grid(row=3, column=0)

entryTelefoneAluno = Entry(root)
entryTelefoneAluno.grid(row=3, column=1)

labelDataAluno = Label(root, text='DataNasc')
labelDataAluno.grid(row=4, column=0)

entryDataAluno = Entry(root)
entryDataAluno.grid(row=4, column=1)

btnAdicionar = Button(root, text='Adicionar', command=adicionar)
btnAdicionar.grid(row=5,column=0, padx=10, pady=10)

btnAdicionar = Button(root, text='Atualizar', command=atualizar)
btnAdicionar.grid(row=5,column=1)




root.mainloop()