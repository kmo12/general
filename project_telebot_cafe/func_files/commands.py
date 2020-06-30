# -*- coding: utf-8 -*-


import func_files.config as config
import func_files.yandex_reviews as yr
import func_files.markups as m

# Интеграция VK API для отправки сообщений админу ТГ канала в ВК
from vk_api_bot.config import admin_id as vk_admin_id
from vk_api_bot.commands import send_message as vk_send_message_module

import datetime


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


def msg_call_to_write_review():
    try:
        config.yandex_corp_id()
    except NameError:
        raise Exception("Не указан Yandex Corporation ID в Config.py")

    return "Отзывы о нашем кафе располагаются на Яндекс площадке. Там же можно написать и своё мнение о нас. " \
           "Пожалуйста, перейдите по ссылке: "  # Далее добавляется markups.yandex_our_corp_link()


def show_yandex_reviews(bot, page: int, chat_id_inner: int, items_on_page: int = 3):
    """
    По очереди посылает 3 сообщения с отзывами
    :param page:
    :param chat_id_inner:
    :param items_on_page:
    :return:
    """
    try:
        config.yandex_corp_id()
    except NameError:
        raise Exception("Не указан Yandex Corporation ID в Config.py")

    reviews = yr.YandexReviews.get_clean_yandex_reviews(config.yandex_corp_id(), page)

    if not reviews:
        bot.send_message(chat_id_inner, "Пока что у нас нет отзывов. Но вы можете нам помочь, оставив первый отзыв!")
        bot.send_message(chat_id_inner, msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())

    if len(reviews) < items_on_page:
        # Закомметировал возможность добавить доп. комментарии к списку, если на выведенном листе 'raw комментов'
        #  не набралось на items_on_page комментов
        # reviews = reviews.extend(yr.YandexReviews.get_clean_yandex_reviews(config.yandex_corp_id(), page + 1))

        items_on_page = len(reviews)

    reviews_in_pack_counter = 0
    for review in reviews:
        bot.send_message(chat_id_inner, review)
        reviews_in_pack_counter += 1
        if reviews_in_pack_counter >= items_on_page:
            break

    return
