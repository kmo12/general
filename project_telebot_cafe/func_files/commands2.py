# -*- coding: utf-8 -*-

from telebot.types import ReplyKeyboardRemove

import func_files.config as config
import func_files.yandex_reviews as yr
import func_files.markups as m

import func_files.calendar_module as t_calendar

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


class TableReservation:
    def __init__(self, bot, user_chat_id):
        self.bot = bot
        self.user_chat_id = user_chat_id
        self.text_for_administrator = None
        self.is_have_result = False

    def start(self, message_object):
        if not self.is_have_result:
            # Изменив строчку можно добавить какое-то вступление к блоку с полной инфой бронирования (первую строчку)
            inner_text_for_administrator = ""

        def ask_date(message_object):
            # TODO Добавляем в reply_markup - calendar
            new_calendar = t_calendar.CallbackData("calendar_1", "action", "year", "month", "day")

            self.bot.send_message(message_object.chat.id, "На какую дату нужен столик? "
                                                          "(Выберите на календаре)",
                                  reply_markup=t_calendar.create_calendar(name=new_calendar.prefix))

            @self.bot.callback_query_handler(func=lambda call: call.data.startswith(new_calendar.prefix))
            def calendar_callback_inline(call: t_calendar.CallbackQuery):
                callback_action_date = t_calendar.callback_inline_handler(bot=self.bot, call=call,
                                                                          uniq_calendar=new_calendar)
                choosed_action = callback_action_date[0]
                choosed_date = callback_action_date[1]

                if choosed_action == "DAY" or choosed_action == "TODAY":
                    msg = self.bot.send_message(
                        chat_id=call.from_user.id,
                        text=f"Выбрана дата: {choosed_date}",
                        reply_markup=ReplyKeyboardRemove())

                    getting_date(msg)

                    log_message(f"Резервирование: Календарь: Выбрана дата: {choosed_date}")

        def getting_date(message_object):
            nonlocal inner_text_for_administrator

            inner_text_for_administrator += f"Дата: {message_object.text.split()[2]}\n"

            ask_time(message_object)

        def ask_time(message_object):
            msg = self.bot.send_message(message_object.chat.id, "На какое время? (Можете ввести в любом формате)")
            self.bot.register_next_step_handler(msg, getting_time)

        def getting_time(message_object):
            nonlocal inner_text_for_administrator

            text = message_object.text

            # TODO Починить проверку. Сейчас при запуске она при принятии сообщения даёт много сообщений подряд.
            # text_without_marks = text.replace(":", "").replace(".", "").replace(" ", "").replace(",", "").replace(";", "")
            # if not text_without_marks.isdecimal():
            #     msg = self.bot.send_message(message_object.chat.id, "Пожалуйста, используйте цифры. Попробуйте ещё раз.")
            #     self.bot.register_next_step_handler(msg, self.getting_time)

            inner_text_for_administrator += f"Время: {text}\n"

            ask_telephone(message_object)

        def ask_telephone(message_object):
            # TODO ПРОВЕРИТЬ reply_markup - запрос предоставить свой телефон. ПОКА НЕ РАБОТАЕТ
            msg = self.bot.send_message(message_object.chat.id,
                                        "Введите ваш телефон в любом формате\n")
            self.bot.register_next_step_handler(msg, getting_telephone)

        def getting_telephone(message_object):
            nonlocal inner_text_for_administrator

            inner_text_for_administrator += f"Телефон: {message_object.text}\n"

            ask_name(message_object)

        def ask_name(message_object):
            msg = self.bot.send_message(message_object.chat.id, "На чьё имя бронируем?")
            self.bot.register_next_step_handler(msg, getting_name)

        def getting_name(message_object):
            nonlocal inner_text_for_administrator

            inner_text_for_administrator += f"Имя: {message_object.text}"

            ask_confirm(message_object)

        def ask_confirm(message_object):
            nonlocal inner_text_for_administrator

            self.bot.send_message(message_object.chat.id, inner_text_for_administrator)
            msg = self.bot.send_message(message_object.chat.id, "Подтверждаете введённые данные?",
                                        reply_markup=m.keyboard_confirm_reservation())
            self.bot.register_next_step_handler(msg, confirm_reservation_callback_handler)

        def confirm_reservation_callback_handler(message_object):
            nonlocal inner_text_for_administrator

            if message_object.text == "Да":
                self.bot.send_message(message_object.chat.id,
                                      "Будем рады вас видеть! Введённые данные будут переданы управляющему и в течение "
                                      "15 минут с вами созвонятся для подтверждения.",
                                      reply_markup=m.reply_start_all_buttons())

                log_message(f"Зарезервировано:\n{inner_text_for_administrator}")

                self.is_have_result = True
                self.text_for_administrator = inner_text_for_administrator

                ############################################################################################
                #                                                                                          #
                #  TODO изучить PostgreSQL и загонять результат туда.                                      #
                #   07.06 Пока что этот скрипт не работает (точнее не могу добиться очередности считывания #
                #   без переноса всех функций в main.py)                                                   #
                #                                                                                          #
                ############################################################################################


            elif message_object.text == "Нет":
                inner_text_for_administrator = None

                self.bot.send_message(message_object.chat.id, "Данные удалены.",
                                      reply_markup=m.reply_start_all_buttons())

            else:
                msg = self.bot.send_message(message_object.chat.id, "Ответьте, пожалуйста, 'Да' или 'Нет'",
                                            reply_markup=m.keyboard_confirm_reservation())
                self.bot.register_next_step_handler(msg, confirm_reservation_callback_handler)

            # # TODO Про изменение данных:
            # #  добавить подтверждение данных: для этого вывести данные, которые готовятся для админа, юзеру.
            # #  Затем спросить "Подтверждаете отправку?" и две inline кнопки "Подтверждаю" и "Изменить данные"
            #
            # # TODO при нажатии на "Изменить данные" нужно прикрутить функционал изменения данных.
            # #  Для этого нужно:
            # #  1) прикрутить keyboard (или inline) кнопки с наименованиями полей
            # #  2) При выборе поля отправлять на метод ask_соответствующее-поле
            # #  3) Прикрутить для всех методов ask_ "standalone" параметр, который не позволит задавать вопросы дальше
            # #  4) После завершения редактирования показать обновлённые данные и переспросить Подтверждение с кнопками
            # #  5) Дополнительно: изменить сохранение данных для отправки админу: возможно создать список с переменными
            # #   и передавать его (здесь же нужно подумать, как и где этот список сохранять, пока он не перестанет быть нужным)

        if not self.is_have_result:
            ask_date(message_object)

        elif self.is_have_result is True:
            return self.text_for_administrator

        else:
            raise Exception("Какая-то проблема с is_have_result!")

        # TODO 07.06
        #  Проблема в том, что функция start() обрабатывается полностью и проскакивает в return,
        #  а telebot медленно по очереди регистрирует действия последовательно
        #  и в итоге start() обработав отдаёт text_for_administrator = "", а телебот собирает инфу хрен знает куда