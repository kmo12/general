import func_files.config as config

from telebot import types


def inline_review_question_for_more():
    """
    Прилагается к сообщению с вопросом "Показать ещё отзывы?" после вывода отзывов.
    :return: types.InlineKeyboardMarkup Object
    """
    # Создаём объект инлайн-клавиатуры
    inline_keyboard = types.InlineKeyboardMarkup()

    # Создаём кнопки
    key_more = types.InlineKeyboardButton(text='Показать ещё', callback_data='/more')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='/no')

    # Добавляем кнопки в инлайн-клавиатуру
    inline_keyboard.add(key_more, key_no)

    return inline_keyboard


def yandex_our_corp_link():
    try:
        config.yandex_corp_id()
    except NameError:
        raise Exception("Не указан Yandex Corporation ID в Config.py")

    link = types.InlineKeyboardMarkup()
    key_link = types.InlineKeyboardButton(text="Все отзывы", url=f"https://yandex.ru/maps/org/{config.yandex_corp_id()}")
    link.add(key_link)

    return link


def reply_start_all_buttons():
    """
    Прилагается к сообщению с вопросом "Показать ещё отзывы?" после вывода отзывов.
    :return: types.ReplyKeyboardMarkup Object
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Забронировать столик")
    btn2 = types.KeyboardButton("Показать отзывы")
    btn3 = types.KeyboardButton("Написать отзыв")  # Вывести сообщение "Напишите отзыв по ссылке на яндекс картах 'ссылка'"
    keyboard.add(btn1, btn2, btn3)

    return keyboard


if __name__ == '__main__':
    pass