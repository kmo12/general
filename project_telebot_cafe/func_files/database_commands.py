# -*- coding: utf-8 -*-


def insert_customer(user_name: str, user_telephone: str, user_telegram_chat_id: int, who_invited: int = None) -> str:
    columns = f"{'user_name, ' if user_name else ''}" \
              f"{'user_telephone, ' if user_telephone else ''}" \
              f"{'user_telegram_chat_id, ' if user_telegram_chat_id else ''}" \
              f"{'who_invited' if who_invited else ''}"
    if columns[-2:] == ", ":
        columns = columns[:-2]

    values = ""
    if user_name:
        values += f"'{user_name}', "
    if user_telephone:
        values += f"'{user_telephone}', "
    if user_telegram_chat_id:
        values += f"{user_telegram_chat_id}, "
    if who_invited:
        values += f"{who_invited}, "
    if values[-2:] == ", ":
        values = values[:-2]

    return f"""INSERT INTO customers({columns})
VALUES
({values})
RETURNING customer_id;
"""


def select_customer_id_chat_id_from_customers():
    return f"""SELECT customer_id, user_telegram_chat_id
FROM customers
"""


def insert_reservation(reservation_date, reservation_time, reservation_telephone, reservation_name, customer_id) -> str:
    return f"""INSERT INTO reservations(reservation_date, reservation_time, reservation_telephone, reservation_name, customer_id)
VALUES
('{reservation_date}', '{reservation_time}', '{reservation_telephone}', '{reservation_name}', {customer_id})
RETURNING reservation_id;
"""


if __name__ == "__main__":
    print(insert_reservation("24-24-2222", "15:55", "89150054444", "name", 5))
