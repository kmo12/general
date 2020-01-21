from random import randint


general_field = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 8, 0, 4, 0],
    [0, 7, 6, 5, 0],
    [0, 0, 0, 0, 0]
]

start_point_y = 2
start_point_x = 2
start_point = general_field[start_point_y][start_point_x]


class MyClass:
    pass


def path_2_top_finder(field, point_x, point_y, admin=0):
    """
    Навигация: (значение в точке; точка Х; точка У)

    :param field: general лист
    :param point_x: "координата" по вложенным листам второго уровня ([][]) внутри general листа
    :param point_y: "координата" по вложенным листам первого уровня([]) внутри general листа
    :param admin: Включение режима отладки
    :return: 
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
        field[point_y - 1][point_x + 1],
        point_y - 1,
        point_x + 1)
    right = (
        field[point_y][point_x + 1],
        point_y,
        point_x + 1)
    bottom_right = (
        field[point_y + 1][point_x + 1],
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


path_2_top_finder(general_field, start_point_x, start_point_y, 1)
