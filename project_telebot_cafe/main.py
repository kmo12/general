# -*- coding: utf-8 -*-

from config import *
import commands

import telebot

bot = telebot.TeleBot(api_token())


def log_message(message):
    print(message)


if __name__ == '__main__':
    log_message("Бот запущен")

    @bot.message_handler(commands=['start'])
    def start_handler(message):
        bot.send_message(message.chat.id, 'Привет, мир!')
        log_message("Бот запущен")


    @bot.message_handler(content_types=['text'])
    def text_handler(message):
        text = message.text.lower()
        chat_id = message.chat.id
        if text == "отзывы":
            bot.send_message(chat_id, f'{commands.get_yandex_company_reviews(13156405625)}')
            log_message(f"Отзывы показаны в чате №{chat_id}")
        else:
            bot.send_message(chat_id, 'Простите, я ваc не понял :(')
            log_message(f"Сообщение не распознано: {message.text}")

    bot.polling(none_stop=False, interval=0, timeout=20)
