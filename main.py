import random
from collections import namedtuple

import telebot
import requests
import os

TOKEN = os.getenv("TOKEN")


from logging_setup import logging

from repositories import get_users_city, insert_user_city, update_user_city

bot = telebot.TeleBot(TOKEN)

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {
    'Yerevan': Coordinates(40.178, 40.505),
}


@bot.message_handler(commands=['start'])
def greet_human(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['get_weather'])
def get_weather(message):
    user_city = get_users_city(message.chat.id)
    logging.info(f'the city {user_city} was requested')

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

    user_city = get_users_city(message.chat.id)
    if user_city:
        update_user_city(message.chat.id, message.text)
    else:
        insert_user_city(message.chat.id, message.text)


bot.polling()