from mysql import connector

connection = connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database = 'aula06'
)

cursor = connection.cursor()

#criando a base de dados

cursor.execute('CREATE database if NOT EXISTS aula8')

'''
cursor.execute('show databases')
for i in cursor:
    print(i)

cursor.execute('use aula8')
'''

# cursor.execute('''CREATE TABLE aluno IF NOT EXISTS(
#     matricula INT PRIMARY KEY AUTO_INCREMENT,
#     nome VARCHAR(30) NOT NULL,
#     idade INT(3),
#     email VARCHAR(40))''')

'''
cursor.execute('show tables')
for i in cursor:
    print(i)

cursor.execute('desc aluno')
for i in cursor:
    print(i)
'''
'''
sql = 'INSERT INTO aluno(nome,idade,email) VALUES("Thereza", 40, "therezaprofessora@gmail.com")'

cursor.execute(sql)
connection.commit()
'''

'''
valores = [
    ('Amanda', 34, 'amanda@gmail.com'),
    ('Bianca', 19, 'bianca@gmail.com'),
    ('Davi', 21, 'davi@gmail.com'),
    ('Felipe', 54, 'felipe@gmail.com'),
    ('Gabriel', 65, 'gabriel@gmail.com'),
    ('Toco', 74, 'toco@gmail.com'),
]

cursor.executemany('INSERT INTO aluno(nome,idade,email) VALUES(%s,%s,%s)',valores)
connection.commit()
print(cursor.rowcount,'Registro(s) inseridos')
'''

'''
cursor.execute('SELECT * FROM aluno')
result = cursor.fetchall()
print('Dados do aluno: ')
for i in result:
    print(i)
'''
'''
cursor.execute('SELECT nome,email FROM aluno')
result = cursor.fetchone()
print('Dados do aluno: ')
for i in result:
    print(i)
'''
'''
cursor.execute('SELECT * FROM aluno WHERE idade > 15')
result = cursor.fetchall()
print('Dados do aluno: ')
for i in result:
    print(i)
'''

cursor.execute('SELECT * FROM aluno ORDER BY nome')
result = cursor.fetchall()
print('Dados do aluno: ')
for i in result:
    print(i)