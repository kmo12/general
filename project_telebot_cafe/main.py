# -*- coding: utf-8 -*-

import func_files.config as config
import func_files.commands2 as cmds
import func_files.markups as m

# import func_files.calendar_module as t_calendar

import telebot

bot = telebot.TeleBot(config.api_token())

all_reservations_by_id = {}

if __name__ == '__main__':
    cmds.log_message("Telegram bot GrandCafe запущен", vk=True)


    # TODO При использовании скрипта более чем 1 человеком global переменная будет ломаться.
    #  Возможное решение: добавить какую-то хэш-таблицу вида {message.chat.id: False} или запись в БД и сверяться с ней
    # is_bot_running = False

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

        if text == "забронировать столик":
            cmds.log_message(f"{all_reservations_by_id}")
            cmds.log_message(f"{all_reservations_by_id.get(str(chat_id))}")
            cmds.log_message(f"*****************************************************")

            if all_reservations_by_id.get(f"{chat_id}") is not None:
                bot.send_message(chat_id, "Резерв на данном аккаунте уже существует, напоминаем:")
                bot.send_message(chat_id, all_reservations_by_id[f"{chat_id}"])

            else:
                all_reservations_by_id[f"{chat_id}"] = cmds.TableReservation(bot, chat_id)
                all_reservations_by_id[f"{chat_id}"].start(message_object)

                all_reservations_by_id[f"{chat_id}"] = all_reservations_by_id[f"{chat_id}"].text_for_administrator

                # reservation_info_maker =
                # reservation_info_maker.start(message_object)


                # TODO на 05.06 проблема в том, что cmds.TableReservation.give_result отдаёт данные в пустоту
                #  и в ячейку словаря приходит None

        elif text == "отзывы" or text == "показать отзывы":
            cmds.show_yandex_reviews(bot, page=1, chat_id_inner=chat_id)

            cmds.log_message(f"Первая страница отзывов показана", chat=chat_id)

            bot.send_message(chat_id, "Показать еще отзывов?", reply_markup=m.inline_review_question_for_more())

            @bot.callback_query_handler(func=lambda call: True)
            def review_callback_for_more(call):
                if call.data == "/more":
                    cmds.show_yandex_reviews(bot, page=2, chat_id_inner=chat_id)
                    bot.send_message(chat_id, cmds.msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())

                    cmds.log_message(f"Вторая страница отзывов показана", chat=chat_id)

                elif call.data == "/no":
                    bot.send_message(chat_id, "Хорошо")
                    return

        elif text == "написать отзыв":
            bot.send_message(chat_id, cmds.msg_call_to_write_review(), reply_markup=m.yandex_our_corp_link())
            cmds.log_message(f"Написать отзыв показано", chat=chat_id)

        else:
            bot.send_message(chat_id, 'Простите, я ваc не понял :(')
            cmds.log_message(f"Сообщение не распознано: {message_object.text}", chat=chat_id)


    bot.infinity_polling()
