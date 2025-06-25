import mysql.connector
from tkinter import *
import tkinter.messagebox as Messagebox

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Senha123@',
    database='teste2av2'
)

cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS teste2av2')
cursor.execute('USE teste2av2')

cursor.execute('''CREATE TABLE IF NOT EXISTS aluno(
               id_aluno INT PRIMARY KEY AUTO_INCREMENT,
               nome VARCHAR(30),
               email VARCHAR(30),
               telefone INT(11),
               data_nascimento VARCHAR(10)
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS curso(
               id_curso INT PRIMARY KEY AUTO_INCREMENT,
               nome_curso VARCHAR(20),
               descricao VARCHAR(20)
               )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS matricula(
               id_matricula INT PRIMARY KEY AUTO_INCREMENT,
               data_matricula VARCHAR(10),
               idAluno INT,
               idCurso INT,
               FOREIGN KEY (idAluno) REFERENCES aluno(id_aluno),
               FOREIGN KEY (idCurso) REFERENCES curso(id_curso)
               )''')

connection.commit()

def adicionar():
    nomeAluno = e_NomeAluno.get()
    emailAluno = e_EmailAluno.get()
    telefoneAluno = e_TelefoneAluno.get()
    dataAluno = e_DataAluno.get()

    if nomeAluno == '' or emailAluno == '' or telefoneAluno == '' or dataAluno == '':
        Messagebox.showerror('Adicionar', 'Preencha todos os campos')
    else:
        cursor.execute('INSERT INTO aluno(nome,email,telefone,data_nascimento) VALUES (%s,%s,%s,%s)', (nomeAluno,emailAluno,telefoneAluno,dataAluno))
        connection.commit()
        Messagebox.showinfo('Adicionar', 'Aluno inserido com sucesso')
        limparCampos()

def visualizar():
    codigoAluno = e_codigoAluno.get()

    try:
        if codigoAluno == '':
            Messagebox.showerror('Visualizar', 'Insira o código do aluno')
        else:
            cursor.execute('SELECT * FROM aluno WHERE id_aluno = %s', (codigoAluno,))
            informacao = cursor.fetchall()
            if not informacao:
                Messagebox.showerror('Visualizar', 'Aluno não encontrado')
            else:
                for i in informacao:
                    Messagebox.showinfo('Visualizar', f'Nome: {i[1]}\nEmail: {i[2]}\nTelefone: {i[3]}\nData Nascimento: {i[4]}')
    except:
        Messagebox.showerror('Visualizar', 'Aluno não encontrado')

def limparCampos():
    e_NomeAluno.delete(0,END)
    e_codigoAluno.delete(0,END)
    e_DataAluno.delete(0,END)
    e_EmailAluno.delete(0,END)
    e_TelefoneAluno.delete(0,END)

def deletar():
    codigoAluno = e_codigoAluno.get()
    try:
        if codigoAluno == '':
            Messagebox.showerror('Deletar', 'Digite o campo obrigatório')
        else:
            cursor.execute('DELETE FROM aluno WHERE id_aluno = %s', (codigoAluno,))
            Messagebox.showinfo('Deletar', 'Aluno deletado com sucesso')
            limparCampos()
    except:
        Messagebox.showerror('Deletar', 'Aluno não encontrado')

def atualizar():
    nomeAluno = e_NomeAluno.get()
    emailAluno = e_EmailAluno.get()
    telefoneAluno = e_TelefoneAluno.get()
    dataAluno = e_DataAluno.get()
    idAluno = e_codigoAluno.get()
    if nomeAluno == '' or emailAluno == '' or telefoneAluno == '' or dataAluno == '' or idAluno == '':
        Messagebox.showerror('Atualizar', 'Todos os campos são obrigatórios')
    else:
        cursor.execute('UPDATE aluno SET nome = %s, email = %s, telefone = %s, data_nascimento = %s WHERE id_aluno = %s', (nomeAluno, emailAluno, telefoneAluno, dataAluno, idAluno))
        Messagebox.showinfo('Atualizar', 'Aluno atualizado com sucesso')
        limparCampos()

root = Tk()
root.geometry('500x500')
root.title('Sistema')

Label(root, text='Cadastrar Aluno').pack()

Label(root, text='Nome').pack()
e_NomeAluno=Entry(root)
e_NomeAluno.pack()

Label(root,text='Email').pack()
e_EmailAluno=Entry(root)
e_EmailAluno.pack()

Label(root,text='Telefone').pack()
e_TelefoneAluno=Entry(root)
e_TelefoneAluno.pack()

Label(root,text='Data nascimento').pack()
e_DataAluno=Entry(root)
e_DataAluno.pack()


btnCadastrar=Button(root, text='Cadastrar', command=adicionar)
btnCadastrar.pack()

btnAtualizar=Button(root, text='Atualizar', command=atualizar)
btnAtualizar.pack()

Label(root,text='Visualizar ou Deletar Aluno').pack()

Label(root,text='Código').pack()
e_codigoAluno=Entry(root)
e_codigoAluno.pack()

btnVisualizar=Button(root,text='Visualizar',command=visualizar)
btnVisualizar.pack()

btnDeletar=Button(root,text='Deletar',command=deletar)
btnDeletar.pack()

root.mainloop()

cursor.close()
connection.close()