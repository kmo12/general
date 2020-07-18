# -*- coding: utf-8 -*-

def test_create_user(name, telephone):
    return f"""INSERT INTO customers(user_name, user_telephone)
VALUES
('{name}', '{telephone}');
"""


def test_create_reservation(date, time, name, telephone, user_id):
    return f"""INSERT INTO reservations(reservation_date, reservation_time, reservation_telephone, reservation_name, user_id)
VALUES
('{date}', '{time}', '{telephone}', '{name}', {user_id})
"""