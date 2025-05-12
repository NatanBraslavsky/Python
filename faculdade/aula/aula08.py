from mysql import connector
import mysql

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'aula8'
)

x = conexao.cursor()

#criando a base de dados ------------------------------

#x.execute('create database if not exists aula8')

#mostrar todas as bases de dados ---------------------
'''
x.execute('show databases')
for i in x:
    print(i)

#usando o banco de dados -------------------------------

x.execute('use aula8')'''

#criar tabela ------------------------------------------
"""
x.execute('''create table if not exists aluno(
          matricula int primary key auto_increment,
          nome varchar(30) not null,
          idade int(3),
          email varchar(40))''')

#mostrar todas as tabelas -----------------------------

x.execute('show tables')
for i in x:
    print(i)

#mostrar a descrição da tabela (desc ou describe)-------------------------

x.execute('desc aluno')
for i in x:
    print(i)

#inserir  dados na tabela - insert into nome da tabela (atributos) values(valores)

y = "insert into aluno(nome,idade,email) values('Thereza',54,'teste@gmail.com')"
x.execute(y)
conexao.commit()
print(x.rowcount,'Registro(s) inserido(s)')

# ---------------------------------------------------------------------------

v = [
    ('José',54,'teste8@gmail.com'),
    ('Tatiana',4,'teste1@gmail.com'),
    ('Adriana',24,'teste2@gmail.com'),
    ('Paulo',19,'teste3@gmail.com'),
    ('Fabiano',85,'teste4@gmail.com'),
    ('Talmo',49,'teste5@gmail.com'),
    ('Maria',4,'teste6@gmail.com'),
    ('Julia',10,'teste7@gmail.com'),
]
x.executemany('insert into aluno(nome,idade,email) values(%s,%s,%s)',v)
conexao.commit()
print(x.rowcount,'Registro(s) inserido(s)')

# seleção simples ------------------------------------------

x.execute('Select * from aluno')
r = x.fetchall()
print('Dados do aluno: ')
for i in r:
    print(i)

x.execute('Select nome,email from aluno')
r = x.fetchall()
print('Dados do aluno: ')
for i in r:
    print(i)

x.execute('Select nome,email from aluno')
r = x.fetchone() #traz somente o primeiro dado da tabela
print('Primeiro nome,email: ')
for i in r:
    print(i)

#seleção condição - where  --------------------------------------

x.execute('select nome from aluno where idade > 15')
r = x.fetchall()
print('Alunos maiores de 15 anos: ')
for i in r:
    print(i)

#Ordenação asc/des - order by ------------------------------------

x.execute('Select * from aluno order by nome ')
r = x.fetchall()
print('Dados do aluno ordenado (A-Z)')
for i in r:
    print(i)

x.execute('Select nome from aluno where idade > 30 order by nome desc')
r = x.fetchall()
print('Dados do aluno ordenado (Z-A)')
for i in r:
    print(i)

#delete - deletar apenas 1 registro ----------------------------------------

x.execute('delete from aluno where matricula=1')
conexao.commit()
print(x.rowcount,'Registro(s) deletado(s)')

#deletar multiplos registros IN  -----------------------------------

r = 'delete from aluno where  matricula in(%s,%s)'
x.execute(r,(2,4))
conexao.commit()
print(x.rowcount,'Registro(s) deletado(s)')

#deletar com intervalo - between ------------------------------------------

r1 = 'delete from aluno where matricula between %s and %s'
x.execute(r1,(6,9))
conexao.commit()
print(x.rowcount,'Registro(s) deletado(s)')

#update - atualizar -------------------------------------------------------

x.execute('update aluno set nome="Tatiana Viana" where matricula=3')
conexao.commit()
print(x.rowcount,'Registro(s) atualizado(s)')"""

#drop  - apaga tudo-------------------------------------------------------

# x.execute('drop database aula8')
# x.execute('drop table aluno')

x.close()
conexao.close()
print('Conexão encerrada')