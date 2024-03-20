# # SQL - structured query language - реляционные базы данных # Postgres # MySQL #  Mariadb # MSSQL
# # SQLite
# # NoSQL: графовые, документоориентированные, Колоночные - Parquet, key-value
#
# # OLTP - бронирование билетов на самолет -- вставка данных в таблицу и получение данных из таблиц
# # / OLAP - analytics # data warehouse # data lake -> data swamp
#
#
# import sqlite3
#
# connection = sqlite3.connect('users.db')
# cursor = connection.cursor()
#
# # res = cursor.execute('''SELECT 1''').fetchone()
# # print(res)
# #
# # CREATE_TABLE_QUERY = '''
# #     CREATE TABLE IF NOT EXISTS user_cities (
# #         chat_id INTEGER PRIMARY KEY,
# #         city TEXT NOT NULL
# #     );
# # '''
# #
# # cursor.execute(CREATE_TABLE_QUERY)
# #
# # INSERT_CITY_QUERY = '''
# #     INSERT INTO user_cities VALUES(?, ?)
# # '''
# # INSERT_PARAMS = (224787, 'Surgut')
#
# # cursor.execute(INSERT_CITY_QUERY, INSERT_PARAMS)
# # connection.commit()
# # connection.rollback()
#
# SELECT_USERS_CITY_QUERY = '''
#     SELECT * FROM user_cities
# '''
# res = cursor.execute(SELECT_USERS_CITY_QUERY, (,)).fetchmany()
# print(res)
#
#
# # REAL - float
# # BLOB binary larige object
# # NUMERIC
#
# # create - создавать
# # read -
# # update
# # delete  # CRUD

# 1999 - SQL
ALTER_TABLE_QUERY_ADD = '''
    ALTER TABLE table_name
    ADD column_name TYPE 
    # None default value = 2 #  3
'''
ALTER_TABLE_QUERY_DROP = '''
    ALTER TABLE table_name
    DROP COLUMN column_name 
'''
DROP_TABLE = '''
    DROP TABLE table_name
'''
TRUNCATE_TABLE = '''TRUNCATE TABLE table_name'''

s = '''
SELECT 
    COUNT(*)
FROM table_name
# WHERE user_city = 'Yerevan' 
GROUP BY user_city 
HAVING 
ORDER BY
LIMIT 10
 '''

'''
select * from user_cities
join cities on user_cities.city_id = cities.id
'''