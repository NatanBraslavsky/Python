import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent #?caminho da pasta que estou
DB_NAME = 'db.sqlite3' #?nome do arquivo sqlite
DB_FILE = ROOT_DIR / DB_NAME #?junção dos dois
TABLE_NAME = 'customers' #?nome da tabela

#*faz a conexão
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(#?executa um comando sqlite(create)
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(' 
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()


##!!delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)#!so para ficar limpando e testando o codigo posterior<³
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()


#*Registrar valores nas colunas da tabela
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:name, :weight)'
)
# cursor.execute(sql, ['Joana', 4])#?anti sql injection
#cursor.executemany(sql, [['Felipe', 8], ['Luiz', 5]])#?adiciona varios
# cursor.execute(sql, {'name': 'Silveira', 'weight': 7.5})#?com dicionario
cursor.executemany(sql, ({'name': 'Silveira', 'weight': 7.5}, {'name' : 'Felipe Rangel', 'weight' : 85.3}))#?com varios dicionarios
connection.commit()


cursor.close()
connection.close()