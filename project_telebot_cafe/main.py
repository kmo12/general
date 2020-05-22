# -*- coding: utf-8 -*-

import func_files.config as config
import func_files.commands as cmds
import func_files.markups as m

import telebot

import datetime

# Интеграция VK API для отправки сообщений админу ТГ канала в ВК
from vk_api_bot.config import admin_id as vk_admin_id
from vk_api_bot.commands import send_message as vk_send_message_module

bot = telebot.TeleBot(config.api_token())


def log_message(*message, chat='No chat ID', vk=False):
    """
    В этой функции настриваются методы отображения логов.
    :param chat: ID чата, в котором было произведено действие
    :param message: набор str, который превратится в одну строчку
    :param vk: Посылать ли указанное сообщение админу в ВК сообщение
    :return: None
    """
    time_now = str(datetime.datetime.now())[:19]
    inner_message = f"({str(chat)})" + " ".join(message)

    print(time_now + ":", inner_message)

    if vk:
        try:
            vk_send_message_module(vk_admin_id(), inner_message)
        except NameError:
            print("Модуль VK API не найден!")


if __name__ == '__main__':
    log_message("Telegram bot GrandCafe запущен", vk=True)

    # TODO При использовании скрипта более чем 1 человеком global переменная будет ломаться.
    #  Возможное решение: добавить какую-то хэш-таблицу вида {message.chat.id: False} или запись в БД и сверяться с ней
    # is_bot_running = False

    @bot.message_handler(commands=['start'])
    def start_handler(message):
        # global is_bot_running
        chat_id = message.chat.id
        bot.send_message(chat_id,
                         "Вас приветствует GrandCafe!\n"
                         "Нужно забронировать столик?\n"
                         "Хочется узнать, что о нас пишут люди в интернете?\n"
                         "Хотите самостоятельно написать отзыв или предложение?\n"
                         "Просто выберите нужный пункт в меню ниже!",
                         reply_markup=m.reply_start_all_buttons())
        log_message("/start", chat=chat_id)
        # TODO изменить эту часть, при /start можно выводить основное кнопочное меню или как-то так

    @bot.message_handler(content_types=['text'])
    def text_handler(message):
        text = message.text.lower()
        chat_id = message.chat.id

        if text == "отзывы" or text == "показать отзывы":
            cmds.show_yandex_reviews(page=1, chat_id_inner=chat_id)

            log_message(f"Первая страница отзывов показана", chat=chat_id)

            bot.send_message(chat_id, "Показать еще отзывов?", reply_markup=m.inline_review_question_for_more())

            @bot.callback_query_handler(func=lambda call: True)
            def review_callback(call):
                if call.data == "/more":
                    cmds.show_yandex_reviews(page=2, chat_id_inner=chat_id)
                    bot.send_message(chat_id, cmds.msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())

                    log_message(f"Вторая страница отзывов показана", chat=chat_id)

                elif call.data == "/no":
                    bot.send_message(chat_id, "Хорошо")
                    return

        elif text == "написать отзыв":
            bot.send_message(chat_id, cmds.msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())
            log_message(f"Написать отзыв показано", chat=chat_id)

        else:
            bot.send_message(chat_id, 'Простите, я ваc не понял :(')
            log_message(f"Сообщение не распознано: {message.text}", chat=chat_id)


    bot.infinity_polling()
