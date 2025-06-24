import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Senha123@',
    database='teste'
)

cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS teste')
cursor.execute('USE teste')

#criação
cursor.execute('''CREATE TABLE IF NOT EXISTS aluno(
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(30),
                idade INT(3)
               )''')

cursor.execute('''
INSERT INTO aluno(nome, idade) VALUES(%s, %s)
''', ('natan', 20))

connection.commit()

cursor.execute('SELECT id FROM aluno WHERE nome = "natan"')
for i in cursor:
    print(i)

cursor.close()
connection.close()