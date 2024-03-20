import sqlite3

from config import DATABASE_NAME

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

CREATE_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS user_cities (
        chat_id INTEGER PRIMARY KEY,
        city TEXT NOT NULL
    );
'''

cursor.execute(CREATE_TABLE_QUERY)
connection.commit()

print('Database successfully initiated')