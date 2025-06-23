from sqlite3 import connect
import mysql.connector
import tkinter as tk

def criar_banco_tabela():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=''
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

    connection.close()
    cursor.close()

criar_banco_tabela()

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Senha123@',
        database='revisaoAV2'
    )

Tk = tk.Tk()