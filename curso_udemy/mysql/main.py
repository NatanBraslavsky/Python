import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        #ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
        
        connection.commit()

        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)'
            )
            data = ('Luiz', 18)
            result = cursor.execute(sql, data)
            # print(sql, data)
            # print(result)
        connection.commit()

        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(name)s, %(age)s)'
            )
            data2 = {
                "name": "Le",
                "age": 27,
            }
            result = cursor.execute(sql, data2)
            # print(sql, data)
            # print(result)
        connection.commit()

        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%(name)s, %(age)s)'
            )
            data2 = (
                {"name": "Sah","age": 33, },
                {"name": "Júlia","age": 74, },
                {"name": "Rose","age": 53, },
            )
            result = cursor.executemany(sql, data2)
            # print(sql, data)
            # print(result)
        connection.commit()

        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)'
            )
            data2 = (
                ("Na", 20),
                ("Vi", 39),
            )
            result = cursor.executemany(sql, data2)
            # print(sql, data)
            # print(result)
        connection.commit()

        with connection.cursor() as cursor:
            sql = (
                f'SELECT * FROM {TABLE_NAME} WHERE id > 3'
            )
            cursor.execute(sql)

            data5 = cursor.fetchall()
            for row in data5:
                print(row)
        
        #!DELETE
        # with connection.cursor() as cursor:
        #     sql = (
        #         f'DELETE FROM {TABLE_NAME}'
        #     )
        #     cursor.execute(sql)
        #     connection.commit()

        with connection.cursor() as cursor:
         sql = (
             f'UPDATE {TABLE_NAME} '
             'SET nome=%s, idade=%s '
             'WHERE id=%s'
         )
         cursor.execute(sql, ('Eleonor', 102, 4))
         connection.commit()