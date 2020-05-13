# -*- coding: utf-8 -*-

from config import *
import commands

import telebot

bot = telebot.TeleBot(api_token())


if __name__ == '__main__':
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'Привет, мир!')


    bot.polling(none_stop=False, interval=0, timeout=20)