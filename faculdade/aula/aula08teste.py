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

#?criação
cursor.execute('''CREATE TABLE IF NOT EXISTS aluno(
                id INT PRIMARY KEY AUTO_INCREMENT,
                nome VARCHAR(30),
                idade INT(3)
               )''')
#?insert
# cursor.execute('''
# INSERT INTO aluno(nome, idade) VALUES(%s, %s)
# ''', ('natan', 20))

# connection.commit()

#?select
cursor.execute('SELECT * FROM aluno')
for i in cursor:
    print(i)

#?update
cursor.execute('UPDATE aluno SET nome="babi" WHERE id = 3')
connection.commit()

#?delete
cursor.execute('DELETE FROM aluno WHERE id BETWEEN 1 and 6')
connection.commit()

cursor.execute('SELECT * FROM aluno WHERE idade >= 18')
x = cursor.fetchall()
for i in x:
    print(i)

cursor.close()
connection.close()