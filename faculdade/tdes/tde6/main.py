import mysql.connector
#!pip install mysql-connector-python

#?Iniciando a conexão
connection = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'NatanBras123@',
    database = 'tde6'
)

#?Criação do cursor, responsável por apontar e selecionar uma linha de dados a partir de um conjunto de resultados
cursor = connection.cursor()

#?Criar o banco 'tde6'
cursor.execute('CREATE DATABASE IF NOT EXISTS tde6')

#?Mostrar os bancos
'''
cursor.execute('SHOW DATABASES')

for i in cursor:
    print(i)
'''

cursor.execute('USE tde6')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS turma(
        id INT PRIMARY KEY AUTO_INCREMENT,
        codigo VARCHAR(10),
        professor VARCHAR(10),
        ano_letivo INT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS aluno(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(30) NOT NULL,
        idade INT,
        email VARCHAR(100),
        turma_id INT,
        FOREIGN KEY(turma_id) REFERENCES turma(id)         
    )
''')

connection.commit()

cursor.execute('show tables')
for i in cursor:
    print(i)

cursor.close()
connection.close()

