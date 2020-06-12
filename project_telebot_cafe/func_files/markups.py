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
    Общие кнопки меню со всеми возможными функциями бота.
    :return: types.ReplyKeyboardMarkup Object
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Забронировать столик")
    btn2 = types.KeyboardButton("Показать отзывы")
    btn3 = types.KeyboardButton("Написать отзыв")
    keyboard.add(btn1, btn2, btn3)

    return keyboard


def keyboard_request_telephone_button():
    # Available in private chats only!
    button = types.ReplyKeyboardMarkup()
    key_telephone = types.KeyboardButton("Отправить свой телефон", request_contact=True)
    button.add(key_telephone)


def inline_confirm_reservation():
    inline_keyboard = types.InlineKeyboardMarkup()

    key_yes = types.InlineKeyboardButton(text='Да', callback_data='/yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='/no')

    inline_keyboard.add(key_yes, key_no)

    return inline_keyboard


def keyboard_confirm_reservation():
    """
    Кнопки для ответа на вопрос о подтверждении резервации столика.
    После выбора опции клавиатура не пропадает!
    :return: types.ReplyKeyboardMarkup Object
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)  #, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    keyboard.add(btn1, btn2)

    return keyboard


if __name__ == '__main__':
    pass
