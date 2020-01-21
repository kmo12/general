from random import randint


general_field = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 8, 0, 4, 0],
    [0, 7, 6, 5, 0],
    [0, 0, 0, 0, 0]
]

start_point_y = 3
start_point_x = 4
start_point = general_field[start_point_y][start_point_x]


# Чтобы не забыть, что нужно будет создать общий класс, для удобного доступа к внутренним функиям этого класса
class MyClass:
    pass
# TODO ?добавить внутрь класса функцию navigation(), чтообы можно было вызывать переменные навигации


def is_destination_available(field, point_x, point_y):
    """
    Проверка точки по "координате" на доступность
    :param field:
    :param point_x:
    :param point_y:
    :return: None, если точка по "координате" не найдена
    Иначе отдаёт координату
    """
    try:
        field_point = field[point_y][point_x]
    except IndexError:
        return None
    else:
        return field_point


def navigation(field, point_x, point_y, admin=0):
    """
    Навигация: (значение в точке; точка Х; точка У)

    :param field: general лист
    :param point_x: "координата" по вложенным листам второго уровня ([][]) внутри general листа
    :param point_y: "координата" по вложенным листам первого уровня([]) внутри general листа
    :param admin: Включение режима отладки
    :return: лист из всех направлений:
    0 - center
    1- top_left
    2- top_top
    3- top_right
    4 - right
    5 - bottom_right
    6 - bottom_bottom
    7 - bottom_left
    8 - left
    """
    center = (
        field[point_y][point_x],
        point_y,
        point_x)
    top_left = (
        field[point_y - 1][point_x - 1],
        point_y - 1,
        point_x - 1)
    top_top = (
        field[point_y - 1][point_x],
        point_y - 1,
        point_x)
    top_right = (
        is_destination_available(field, point_x + 1, point_y - 1), #
        point_y - 1,
        point_x + 1)
    right = (
        is_destination_available(field, point_x + 1, point_y), #
        point_y,
        point_x + 1)
    bottom_right = (
        is_destination_available(field, point_x + 1, point_y + 1), #
        point_y + 1,
        point_x + 1)
    bottom_bottom = (
        field[point_y + 1][point_x],
        point_y + 1,
        point_x)
    bottom_left = (
        field[point_y + 1][point_x - 1],
        point_y + 1,
        point_x - 1)
    left = (
        field[point_y][point_x - 1],
        point_y,
        point_x - 1)

    # Вывод при включении режима отладки (admin=1)
    if admin:
        print(f"{center=}")
        print(f"{top_left=}")
        print(f"{top_top=}")
        print(f"{top_right=}")
        print(f"{right=}")
        print(f"{bottom_right=}")
        print(f"{bottom_bottom=}")
        print(f"{bottom_left=}")
        print(f"{left=}")

    return center, top_left, top_top, top_right, right, bottom_right, bottom_bottom, bottom_left, left


def which_way():
    """
    Делает выбор, какая точка "больше" (в какую *сторону* двигаться?)
    :return:
    """



navigation(general_field, start_point_x, start_point_y, 1)

nav_testing = navigation(general_field, start_point_x, start_point_y)

print(nav_testing)

# Проверка, нужно ли рассматривать точку для передвижения на неё
if isinstance(nav_testing[2][0], (int, float)):
    pass
