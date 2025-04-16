import sqlite3
from main import DB_FILE, TABLE_NAME

#*faz a conexão
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#?selecionar todos
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()


#?selecionar um
cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "1"')

row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()