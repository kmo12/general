from random import randint


general_field = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 8, 0, 4, 0],
    [0, 7, 6, 5, 0],
    [0, 0, 0, 0, 0]
]

start_point_y = 1
start_point_x = 1
start_point = general_field[start_point_y][start_point_x]


class MyClass:
    pass


def path_2_top_finder(field, point_x, point_y, admin=0):
    # Ориентация в пространстве
    center = field[point_y][point_x]
    top_left = field[point_y - 1][point_x - 1]
    top_top = field[point_y - 1][point_x]
    top_right = field[point_y - 1][point_x + 1]
    right = field[point_y][point_x + 1]
    bottom_right = field[point_y + 1][point_x + 1]
    bottom_bottom = field[point_y + 1][point_x]
    bottom_left = field[point_y + 1][point_x - 1]
    left = field[point_y][point_x - 1]

    # Режим отладки
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

