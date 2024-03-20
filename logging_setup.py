import logging
import os

import telebot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(
    level=logging.DEBUG,
    filename='bot.log',
    filemode='w',
    format='%(name)s => %(levelname)s => %(message)s => %(asctime)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

my_formatter = logging.Formatter(
    '%(name)s => %(message)s => %(asctime)s',
    datefmt='%Y/%m/%d %H:%M:%S',
)


class TelegramBotHandler(logging.Handler):
    def __init__(self, token, chat_id):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record):
        bot = telebot.TeleBot(self.token)
        bot.send_message(self.chat_id, self.format(record))


class AntiTestFilter(logging.Filter):
    def filter(self, record):
        return not record.msg.lower().startswith('test:')


# handlers
file_handler = logging.FileHandler(filename='critical.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(my_formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(my_formatter)

telegram_handler = TelegramBotHandler(TOKEN, CHAT_ID)
telegram_handler.setFormatter(my_formatter)
telegram_handler.setLevel(logging.CRITICAL)

root_handler = logging.getLogger()

root_handler.addHandler(file_handler)
root_handler.addHandler(console_handler)
root_handler.addHandler(telegram_handler)

root_handler.addFilter(AntiTestFilter())
