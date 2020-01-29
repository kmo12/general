# Мой первый тестовый модуль для встраивания в первую игру
from random import randint
import re
import sys
from functools import reduce


__name__ = 'Guess The Num Functional!'
__version__ = '1.0'

# Функция проверяет ответ по вопросу о правилах
def checking_ques(func_starter_ques):
    """
    Проверка ответа на вопрос при приветствии.

    Эта функция нужна для того, чтобы проверять ответ "Показать правила или сразу начать игру?"
    и возвращать True, если ответ о желании увидеть правила положительный.
    :param func_starter_ques:
    :return:
    """
    if func_starter_ques == "Правила":
        return True
    elif func_starter_ques == "правила":
        return True
    elif func_starter_ques == "0":
        return True

# Функция проверяет ответ по вопросу о сложности и ЗАДАЁТ СЛОЖНОСТЬ
def checking_difficulty(difficulty_func):
    """
    Проверка ответа в выборе сложности.
    +Здесь задаётся сложность

    Эта функция проверяет ответ на вопрос "Какой уровень сложности выбрать?"
    и возвращает :number, rand_number_from, rand_number_until:.
    Также в этой функции можно изменить значения у каждой сложности.
    rand_number_from - От какого числа
    rand_number_until - До какого числа
    :param difficulty_func:
    :return:
    """
    if difficulty_func == "1":

        rand_number_from = 1
        rand_number_until = 5

    elif difficulty_func == "2":

        rand_number_from = 1
        rand_number_until = 10

    elif difficulty_func == "3":

        rand_number_from = 1
        rand_number_until = 25

    else:
        return False

    number = randint(rand_number_from, rand_number_until)
    return number, rand_number_from, rand_number_until


def is_input_int():
    # Эта функция обязана быть в основном файле с кодом, а не в отдельном модуле, иначе выдаёт ошибку, что answer не задан
    """
    Старая функция, которая потеряла свою необходимость,
    из-за изученного модуля ''.isdigit()

    Выводит input и проверяет, было ли введено целое число.

    Параметр не указывается. Функция создаёт global answer
    и присваивает ему целочисленное значение input,
    перед этим заставив написать именно целое число.
    :return answer:
    """
    global answer

    while True:  # Проверяем, было ли введено число
        answer = input("Введите число: ")
        try:
            answer = int(answer)
            break
        except ValueError:
            print("")
            print("Пожалуйста, введите целое число")
    return answer


if __name__ == "__main__":
    print("Это файл с 'мозгами' замечательной игры 'Guess The Num!'")
