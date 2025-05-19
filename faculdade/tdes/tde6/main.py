import mysql.connector
from tabulate import tabulate 
#!pip install mysql-connector-python

#?Iniciando a conexão
connection = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'senha123@',
    database = ''
)

#?Criação do cursor, responsável por apontar e selecionar uma linha de dados a partir de um conjunto de resultados
cursor = connection.cursor()

#?Criar o banco 'tde6'
# cursor.execute('CREATE DATABASE IF NOT EXISTS tde6')

#?Mostrar os bancos
# cursor.execute('SHOW DATABASES')

# for i in cursor:
#     print(i)

#?Usar banco de dados
# cursor.execute('USE tde6')

#?Criar tabela
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS turma(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         professor VARCHAR(10),
#         ano_letivo INT
#     )
# ''')

# #?Criar tabela
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS aluno(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         nome VARCHAR(30) NOT NULL,
#         idade INT,
#         email VARCHAR(100),
#         turma_id INT,
#         FOREIGN KEY(turma_id) REFERENCES turma(id)         
#     )
# ''')
# connection.commit()

#?Mostrar tabelas
'''
cursor.execute('show tables')
for i in cursor:
    print(i)
'''

#?Adicionando elementos professor
# valores_professor = [
#     ('Mauricio', 1981),
#     ('João', 1990),
#     ('José', 2000)
# ]

# cursor.executemany('INSERT INTO turma(professor, ano_letivo) VALUES(%s, %s)', valores_professor)

# connection.commit()


#?Adicionando elementos aluno
# valores_alunos = [
#     ('Natan', 20, 'natanbraslavsky1@gmail.com', 1),
#     ('Enzo', 20, 'enzoribastorres@gmail.com', 2),
#     ('Felipe', 45, 'felipe@hotmail.com', 2),
#     ('Alice', 55, 'Alicegostosinha123@gmail.com', 1),
#     ('Vicente', 80, 'vicentevelhopirocudo@outlook.com', 3)
# ]

# cursor.executemany('INSERT INTO aluno(nome, idade,email,turma_id) VALUES (%s, %s, %s, %s)', valores_alunos)

# connection.commit()


# ?Mostrar informações professor
# cursor.execute('''
#     SELECT id, professor, ano_letivo FROM turma
# ''')
# result = cursor.fetchall()
# for i in result:
#     print(i) 

#?Mostrar informações aluno
# print("Alunos")
# cursor.execute('''SELECT * FROM aluno''')
# result = cursor.fetchall()
# headers = ['ID', 'Nome', 'Idade', 'Email', 'Turma_ID']
# print(tabulate(result, headers=headers, tablefmt='grid'))
# print()

#?Mostrar informações aluno por id_turma
# consulta_aluno = int(input("Digite o id da turma: "))
# cursor.execute('SELECT * FROM aluno WHERE turma_id = (%s)', (consulta_aluno,))
# result = cursor.fetchall()
# headers = ['ID', 'Nome', 'Idade', 'Email', 'Turma_ID']
# if cursor.rowcount:
#     print()
#     print(f"Alunos com a turma de id {consulta_aluno}")
#     print(tabulate(result, headers=headers, tablefmt='grid'))
        
# else: 
#     print("Id não encontrado, ou aluno não cadastrado na turma.")


#?Update email aluno
# cursor.execute("UPDATE aluno SET email='natanbraslavsky2@gmail.com' WHERE id = 16")
# connection.commit()

#?Deletar um aluno
# cursor.execute("DELETE FROM aluno WHERE id = 19")
# connection.commit()

#?Mostrar alunos com idade decrescente
# cursor.execute("SELECT * FROM aluno ORDER BY idade DESC")
# result = cursor.fetchall()
# for i in result:
#     print(i)

#?Dropando a tabela
# cursor.execute("DROP TABLE aluno")
# cursor.execute("DROP TABLE turma")

#?Dropando o database
# cursor.execute("DROP DATABASE tde6")
# cursor.execute

cursor.close()
connection.close()

