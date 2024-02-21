import random
from collections import namedtuple
import sqlite3

import telebot
import requests
import settings

bot = telebot.TeleBot(settings.TOKEN)

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {
    'Yerevan': Coordinates(40.178, 40.505),
}


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

@bot.message_handler(commands=['start'])
def greet_human(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['get_weather'])
def get_weather(message):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    res = cursor.execute(SELECT_USERS_CITY_QUERY, (message.chat.id,)).fetchone()
    user_city = None
    if res:
        user_city = res[0]

    if user_city and user_city in cities:
        coordinates = cities[user_city]
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={settings.WEATHER_API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.json()
            bot.send_message(message.chat.id, weather["weather"][0]["description"])
        else:
            bot.send_message(message.chat.id, 'Сервис определния погоды недоступен, пожалуйста, попробуйте позже')
    else:
        bot.send_message(message.chat.id, 'Нет данных для определения погоды. Пожалуйста, выполните настрйоку через команду setup или '
                                          'подождите пока ваш город будет добавлен в словарь ')


@bot.message_handler(commands=['get_fox'])
def get_fox(message):
    url = f'https://randomfox.ca/images/{random.randint(1, 100)}.jpg'
    bot.send_photo(message.chat.id, url)


@bot.message_handler(commands=['setup'])
def ask_city(message):
    bot.send_message(message.chat.id, 'В каком городе вы живете?')
    bot.register_next_step_handler(message, proceed_city)


def proceed_city(message):
    bot.send_message(message.chat.id, f'Какой хороший город - {message.text}!')

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    res = cursor.execute(SELECT_USERS_CITY_QUERY, (message.chat.id,)).fetchone()
    if res:
        cursor.execute(UPDATE_USER_CITY_QUERY, (message.text, message.chat.id))
    else:
        cursor.execute(INSERT_CITY_QUERY, (message.chat.id, message.text))

    connection.commit()


bot.polling()