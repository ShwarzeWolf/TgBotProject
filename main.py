import telebot
import requests
import settings

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def greet_human(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['get_weather'])
def get_weather(message):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={40.178}&lon={40.505}&appid={settings.WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        bot.send_message(message.chat.id, weather["weather"][0]["description"])
    else:
        bot.send_message(message.chat.id, 'Сервис определния погоды недоступен, пожалуйста, попробуйте позже')


bot.polling()