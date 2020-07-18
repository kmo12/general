# -*- coding: utf-8 -*-

import func_files.config as config
import func_files.commands as cmds
import func_files.markups as m
import func_files.calendar_module as t_calendar

import func_files.pg_database_execution as pg_db_executor
import func_files.database_commands as db_command

import telebot
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot(config.api_token())

all_reservations_by_id = {}

if __name__ == '__main__':
    cmds.log_message("Telegram bot GrandCafe запущен", vk=True)

    # Create connection with PostgreSQL DataBase
    db_info = config.pg_db_connection_info()
    db_executor = pg_db_executor.PGDataBaseExecutor(db_info[0],  # database
                                                    db_info[1],  # user
                                                    db_info[2],  # password
                                                    db_info[3],  # host
                                                    db_info[4],  # port
                                                    )

    @bot.message_handler(commands=['start'])
    def start_handler(message):
        chat_id = message.chat.id
        bot.send_message(chat_id,
                         "Вас приветствует GrandCafe!\n"
                         "Нужно забронировать столик?\n"
                         "Хочется узнать, что о нас пишут люди в интернете?\n"
                         "Хотите самостоятельно написать отзыв или предложение?\n"
                         "Просто выберите нужный пункт в меню ниже!",
                         reply_markup=m.reply_start_all_buttons())
        cmds.log_message("/start", chat=chat_id)
        # TODO изменить эту часть, при /start можно выводить основное кнопочное меню или как-то так


    @bot.message_handler(content_types=['text'])
    def text_handler(message_object):
        text = message_object.text.lower()
        chat_id = message_object.chat.id
        user_id = message_object.from_user.id

        if text == "забронировать столик":
            # Логи
            cmds.log_message(f"{all_reservations_by_id}")
            cmds.log_message(f"{all_reservations_by_id.get(str(user_id))}")
            cmds.log_message(f"*****************************************************")

            # Проверяем, если ли запись брони для этого пользователя
            if all_reservations_by_id.get(f"{user_id}") is not None:
                bot.send_message(chat_id, "Резерв на данном аккаунте уже существует, напоминаем:")
                msg = bot.send_message(chat_id, all_reservations_by_id[f"{user_id}"],
                                       reply_markup=m.keyboard_reservation_abort())

                def done_reservation_callback_handler(message_object):
                    if message_object.text == "Отменить бронирование":
                        all_reservations_by_id[f"{message_object.chat.id}"] = None
                        bot.send_message(message_object.chat.id,
                                         "Данные удалены.",
                                         reply_markup=m.reply_start_all_buttons())

                        cmds.log_message(f"Данные {message_object.chat.id} удалены.")

                    elif message_object.text == "Ничего не делать":
                        # bot.edit_message_reply_markup(message_object.chat.id, message_object.message_id, reply_markup=m.reply_start_all_buttons())
                        bot.send_message(message_object.chat.id,
                                         "Хорошо.",
                                         reply_markup=m.reply_start_all_buttons())

                    # TODO Сюда добавить функционал изменения данных, когда будет прикручен функционал БД

                bot.register_next_step_handler(msg, done_reservation_callback_handler)


            else:
                # Спрашиваем дату
                new_calendar = t_calendar.CallbackData("calendar_1", "action", "year", "month", "day")
                bot.send_message(message_object.chat.id, "На какую дату нужен столик? "
                                                         "(Выберите на календаре)",
                                 reply_markup=t_calendar.create_calendar(name=new_calendar.prefix))

                # Обрабатываем выбранную на календаре дату
                @bot.callback_query_handler(func=lambda call: call.data.startswith(new_calendar.prefix))
                def calendar_callback_inline(call: t_calendar.CallbackQuery):
                    callback_action_date = t_calendar.callback_inline_handler(bot=bot, call=call,
                                                                              uniq_calendar=new_calendar)
                    choosed_action = callback_action_date[0]
                    choosed_date = callback_action_date[1]

                    if choosed_action == "DAY" or choosed_action == "TODAY":
                        msg = bot.send_message(
                            chat_id=call.from_user.id,
                            text=f"Выбрана дата: {choosed_date}",
                            reply_markup=ReplyKeyboardRemove())

                        cmds.log_message(f"Резервирование: Календарь: Выбрана дата: {choosed_date}")
                        getting_date_asking_time(msg)

                def getting_date_asking_time(message_object):
                    all_reservations_by_id[f"{message_object.chat.id}"] = f"Дата: {message_object.text.split()[2]}\n"

                    print(
                        f"all_reservations_by_id[f'{message_object.chat.id}'] {all_reservations_by_id[f'{message_object.chat.id}']}")

                    msg = bot.send_message(message_object.chat.id,
                                           "На какое время? (Можете ввести в любом формате)")
                    bot.register_next_step_handler(msg, getting_time_asking_telephone)

                def getting_time_asking_telephone(message_object):
                    # TODO Добавить проверку корректности времени.
                    all_reservations_by_id[f"{message_object.chat.id}"] += f"Время: {message_object.text}\n"

                    print(all_reservations_by_id[f"{message_object.chat.id}"])

                    # TODO Добавить в reply_markup запрос предоставить свой телефон одной кнопкой.
                    msg = bot.send_message(message_object.chat.id,
                                           "Введите ваш телефон в любом формате\n")
                    bot.register_next_step_handler(msg, getting_telephone_asking_name)

                def getting_telephone_asking_name(message_object):
                    # TODO Добавить проверку корректности телефона.
                    all_reservations_by_id[f"{message_object.chat.id}"] += f"Телефон: {message_object.text}\n"

                    msg = bot.send_message(message_object.chat.id, "На чьё имя бронируем?")
                    bot.register_next_step_handler(msg, getting_name_asking_confirm)

                def getting_name_asking_confirm(message_object):
                    # TODO Добавить проверку корректности имени (чтобы не было цифр).
                    all_reservations_by_id[f"{message_object.chat.id}"] += f"Имя: {message_object.text}"

                    bot.send_message(message_object.chat.id, all_reservations_by_id[f"{message_object.chat.id}"])
                    msg = bot.send_message(message_object.chat.id, "Подтверждаете введённые данные?",
                                           reply_markup=m.keyboard_confirm_reservation())
                    bot.register_next_step_handler(msg, confirm_reservation_callback_handler)

                def confirm_reservation_callback_handler(message_object):
                    if message_object.text == "Да":
                        cmds.log_message(f"Зарезервировано:\n{all_reservations_by_id[f'{message_object.chat.id}']}")



                        bot.send_message(message_object.chat.id,
                                         "Будем рады вас видеть! Введённые данные будут переданы управляющему и в течение "
                                         "15 минут с вами созвонятся для подтверждения.",
                                         reply_markup=m.reply_start_all_buttons())

                    elif message_object.text == "Нет":
                        bot.send_message(message_object.chat.id,
                                         "Данные удалены.",
                                         reply_markup=m.reply_start_all_buttons())
                        cmds.log_message(f"Отмена резерва:\n{all_reservations_by_id[f'{message_object.chat.id}']}")

                        # TODO Про изменение данных:
                        #  добавить подтверждение данных: для этого вывести данные, которые готовятся для админа, юзеру.
                        #  Затем спросить "Подтверждаете отправку?" и две inline кнопки "Подтверждаю" и "Изменить данные"

                        # TODO при нажатии на "Изменить данные" нужно прикрутить функционал изменения данных.
                        #  Для этого нужно:
                        #  1) прикрутить keyboard (или inline) кнопки с наименованиями полей
                        #  2) При выборе поля отправлять на метод ask_соответствующее-поле
                        #  3) Прикрутить для всех методов ask_ "standalone" параметр, который не позволит задавать вопросы дальше
                        #  4) После завершения редактирования показать обновлённые данные и переспросить Подтверждение с кнопками
                        #  5) Дополнительно: изменить сохранение данных для отправки админу: возможно создать список с переменными
                        #   и передавать его (здесь же нужно подумать, как и где этот список сохранять, пока он не перестанет быть нужным)

                    else:
                        msg = bot.send_message(message_object.chat.id, "Напишите, пожалуйста, 'Да' или 'Нет'",
                                               reply_markup=m.keyboard_confirm_reservation())
                        bot.register_next_step_handler(msg, confirm_reservation_callback_handler)

        elif text == "отзывы" or text == "показать отзывы":
            bot.send_message(message_object.chat.id,
                             "К сожалению, сейчас такая возможность недоступна. Мы уже работаем над решением проблемы.",
                             reply_markup=m.reply_start_all_buttons())

            # TODO До 07.06 нормально работало, а потом сломалось. Выдаёт ошибку:

            # File "/home/akakii95/project_telebot_cafe/func_files/yandex_reviews.py", line 61, in get_yandex_company_raw_revie
            # ws
            #     result = json.loads(r.content)
            #   File "/usr/lib/python3.7/json/__init__.py", line 348, in loads
            #     return _default_decoder.decode(s)
            #   File "/usr/lib/python3.7/json/decoder.py", line 337, in decode
            #     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
            #   File "/usr/lib/python3.7/json/decoder.py", line 355, in raw_decode
            #     raise JSONDecodeError("Expecting value", s, err.value) from None
            # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
            # "

            # cmds.show_yandex_reviews(bot, page=1, chat_id_inner=chat_id)
            #
            # cmds.log_message(f"Первая страница отзывов показана", chat=chat_id)
            #
            # bot.send_message(chat_id, "Показать еще отзывов?", reply_markup=m.inline_review_question_for_more())
            #
            # @bot.callback_query_handler(func=lambda call: True)
            # def review_callback_for_more(call):
            #     if call.data == "/more":
            #         cmds.show_yandex_reviews(bot, page=2, chat_id_inner=chat_id)
            #         bot.send_message(chat_id, cmds.msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())
            #
            #         cmds.log_message(f"Вторая страница отзывов показана", chat=chat_id)
            #
            #     elif call.data == "/no":
            #         bot.send_message(chat_id, "Хорошо")
            #         return

        elif text == "написать отзыв":
            bot.send_message(chat_id, cmds.msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())
            cmds.log_message(f"Написать отзыв показано", chat=chat_id)

        elif "привет" in text:
            bot.send_message(chat_id, 'Доброго времени суток!', reply_markup=m.reply_start_all_buttons())

        else:
            bot.send_message(chat_id, 'Простите, я ваc не понял :(', reply_markup=m.reply_start_all_buttons())
            cmds.log_message(f"Сообщение не распознано: {message_object.text}", chat=chat_id)


    bot.infinity_polling()
