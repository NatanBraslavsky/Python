import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='senha123@',
    database=''
)

cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS livraria')



connection.close()
cursor.close()