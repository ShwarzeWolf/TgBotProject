import sqlite3

from config import DATABASE_NAME

INSERT_CITY_QUERY = '''
    INSERT INTO user_cities VALUES(?, ?)
'''
SELECT_USERS_CITY_QUERY = '''
    SELECT city FROM user_cities
    WHERE chat_id = (?)
'''
UPDATE_USER_CITY_QUERY = '''
    UPDATE user_cities SET city = (?) 
    WHERE chat_id = (?)
'''


def get_users_city(user_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    res = cursor.execute(SELECT_USERS_CITY_QUERY, (user_id,)).fetchone()
    if res:
        return res[0]


def update_user_city(user_id, new_city):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(UPDATE_USER_CITY_QUERY, (new_city, user_id))

    connection.commit()


def insert_user_city(user_id, city):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(INSERT_CITY_QUERY, (user_id, city))

    connection.commit()
