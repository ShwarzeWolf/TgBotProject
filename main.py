import random
from collections import namedtuple

import telebot
import requests
import settings

bot = telebot.TeleBot(settings.TOKEN)

Coordinates = namedtuple('Coordinates', ('latitude', 'longitude'))
cities = {
    'Yerevan': Coordinates(40.178, 40.505),
}


@bot.message_handler(commands=['start'])
def greet_human(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['get_weather'])
def get_weather(message):
    coordinates = cities['Yerevan']
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={settings.WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        bot.send_message(message.chat.id, weather["weather"][0]["description"])
    else:
        bot.send_message(message.chat.id, 'Сервис определния погоды недоступен, пожалуйста, попробуйте позже')


@bot.message_handler(commands=['get_fox'])
def get_fox(message):
    url = f'https://randomfox.ca/images/{random.randint(1, 100)}.jpg'
    bot.send_photo(message.chat.id, url)


bot.polling()