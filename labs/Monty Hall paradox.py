# Участнику игры нужно выбрать одну из трёх дверей. За одной из дверей находится приз,
# за двумя другими дверями ничего нет. Участник выбирает одну из дверей, например,
# номер 1, после этого ведущий, который знает, где находится приз, открывает одну из
# оставшихся дверей, например, номер 3, за которой ничего нет. После этого он спрашивает
# участника: не желаете ли он изменить свой выбор и выбрать дверь номер 2? Участник
# может согласиться либо остаться при своём выборе.

# Увеличиваются ли шансы участника выиграть приз, если он примет предложение
# ведущего и измените свой выбор?
from random import randint


def monty_hall_general():
    change_yes_win = 0
    # При каждом запуске генерируем случайную победную дверь
    win_door = randint(1, 3)
    # При каждом запуске генерируем случайную выбранную дверь
    picked_door = randint(1, 3)

    # Если сразу угадали, то skip, если нет, то проверяем
    if picked_door != win_door:
        for i in range(1, 4):
            # Перебором по каждой двери отбираем единственную подходящую, при смене решения на которой принесёт нам победу
            # (эта дверь не должна быть победной и не должна быть выбрана игроком,
            # то есть пустая. Меняя свой выбор, на ней мы побеждаем)
            if i != win_door and i != picked_door:
                change_yes_win = 1

    return change_yes_win


total_change_yes_win = 0

# Количество прогонов и-гр
N = 1000

for _ in range(N):

    # Прибавляем к общему количеству *побед от смены* результат функции
    total_change_yes_win += monty_hall_general()

    # picked_door = randint(1, 3)
    # win_door = randint(1, 3)
    # Выбор: менять ли решение об открытии первой двери / 0 нет / 1 да
    # change_choosing = 1  # randint(0, 1)

    # if picked_door == 1:
    #     if win_door == 2:
    #         # Показываю, что за дверью №3 пусто. Меняем?
    #         if change_choosing == 1:
    #             # Да, меняем
    #             changeYes_win += 1
    #         else:
    #             changeYes_fail += 1
    #     elif win_door == 3:
    #         # Показываю, что за дверью №2 пусто. Меняем?
    #         if change_choosing == 1:
    #             # Да, меняем
    #             changeYes_win += 1
    #         else:
    #             changeYes_fail += 1
    #
    # if picked_door == 2:
    #     if win_door == 1:
    #         # Показываю, что за дверью №3 пусто. Меняем?
    #         if change_choosing == 1:
    #             # Да, меняем
    #             changeYes_win += 1
    #         else:
    #             changeYes_fail += 1
    #     elif win_door == 3:
    #         # Показываю, что за дверью №1 пусто. Меняем?
    #         if change_choosing == 1:
    #             # Да, меняем
    #             changeYes_win += 1
    #         else:
    #             changeYes_fail += 1
    #
    # if picked_door == 3:
    #     if win_door == 1:
    #         # Показываю, что за дверью №2 пусто. Меняем?
    #         if change_choosing == 1:
    #             # Да, меняем
    #             changeYes_win += 1
    #         else:
    #             changeYes_fail += 1
    #     elif win_door == 2:
    #         # Показываю, что за дверью №1 пусто. Меняем?
    #         if change_choosing == 1:
    #             # Да, меняем
    #             changeYes_win += 1
    #         else:
    #             changeYes_fail += 1

print(f"\ntotal_change_yes_win = {total_change_yes_win} \\ {N}")
print("Шанс с Да:", (total_change_yes_win / N) * 100, "%")