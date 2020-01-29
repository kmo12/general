from builtins import print
import Guess_The_Num.guess_the_num_functions as gtn
import sys
import re
from functools import reduce

# TODO не забыть перенести все функции в отдельный файл guess_the_num_functions
def login_signup_asking():
    # Задаём переменную текущего пользователя.
    active_user = ()
    # active_user[0] - Логин
    # active_user[1] - Пароль
    # active_user[2] - Имя

    db_log_pass_file = r"F:\PyCharm ФАЙЛЫ проектов и прочего\Проекты\Guess_The_Num\database\login-pass.txt"
    success = 0  # Если 1, то выходим из цикла вопроса логина/регистрации (нужно для того, чтобы вернуться из регистрации)

    # Просим залогиниться/зарегистрироваться/зайти как гость
    while not success:
        login_signup_question = input("""
Для сохранения статистики, пожалуйста, залогиньтесь.
[1] или [login] - Зайти под своими данными
[9] или [sign up] - Зарегистрировать нового пользователя
    
[0] или [guest] - Для гостевого входа (статистика не записывается)
    
Что делаем?: """)

        if login_signup_question == "1" or login_signup_question == "login":
            # Вводим логин + проверяем ввод на пустотность и наличие в базе
            while True:
                ask_for_login = input("Введите логин: ")
                if not ask_for_login:
                    print("Введён пустой логин!")
                    continue
                elif not login_pass_checker(ask_for_login, db_log_pass_file):
                    print("\nПользователя с таким логином не существует! Пожалуйста, повторите ввод.\n")
                    continue
                break
            # Вводим пароль + проверяем ввод на пустотность
            while True:
                ask_for_password = input("Введите пароль: ")
                if not ask_for_password:
                    print("Введён пустой пароль!")
                    continue

                active_user = login_pass_checker(ask_for_login, db_log_pass_file, ask_for_password)
                active_user[3] = int(re.search(r"^\d+", active_user[3]).group())

                if not login_pass_checker(ask_for_login, db_log_pass_file, ask_for_password):
                    print("\nПароль не подходит. Пожалуйста, повторите ввод.\n")
                    continue

                print(f"\nВход под логином {active_user[0]} успешно выполнен!\n")
                success = 1
                break


# TODO разбить login и sign up на разные функции, чтобы легко ввести "Такого логина не существует, зарегистрировать его?"
#  и "Такой логин уже существует, выполнить вход?
#  (дополнительым параметром в этих функциях добавить логин, чтобы повторно не вбивать после переброса)
        elif login_signup_question == "9" or login_signup_question == "sign up":
            while True:
                new_person_login = input("Введите логин нового пользователя: ")
                # Проверяем логин на пустотность (выводим на вопрос логин/регистрация)
                #  и на существование в базе
                if not new_person_login:
                    break  # Возвращаемся на текст вопроса о логине/регистрации
                elif login_pass_checker(new_person_login, db_log_pass_file):
                    print("\nПользователь с таким логином уже существует!\n"
                          "Чтобы прекратить процесс регистрации и войти под своим логином, нажмите [Enter] "
                          "в поле ввода нового логина.\n")
                    continue

                new_person_password = input("Введите пароль нового пользователя: ")
                new_person_name = input("Введите имя: ")

                active_user = sign_up(new_person_login, new_person_password, new_person_name, db_log_pass_file)

                if not active_user:
                    print("Что-то пошло не так, попробуйте снова.")
                    continue

                print(f"Пользователь с данными {active_user[0]} : {active_user[1]} ({active_user[2]}) успешно создан!\n"
                      f"Вход в систему выполнен по новым данным.")
                success = 1
                break

        elif login_signup_question in ("guest", "0"):
            active_user = (None, None, "Гость", 0)
            success = 1

        if login_signup_question not in ("9", "sign up", "1", "login", "0", "guest", "0"):
            print("\nТакой команды не существует!")

    print(f"\nУспешно отработали функцию login_signup_asking().\nactive_user = {active_user}. Начинаем игру!\n")  # Сюда добавить код, который исполняется после регистрации/логина
    return active_user

# TODO далее, если логин найден, то переходим к такому же поиску, но пароля по файлу с паролями (используя другую функцию)
#  если логин не найден, то return print("Такой логин не зарегистрирован") (или подумать над return continue
#  для цикла проверки ввода в функции login_signup_asking())


def sign_up(np_login, np_password, np_name, np_login_password_path):
    if np_login and np_password:
        with open(np_login_password_path, "a", encoding="utf-8") as signup_login_pass_file:
            signup_login_pass_file.write(f"{np_login}:{np_password}:{np_name}:0\n")  # 0 = start num of wins
            return (np_login, np_password, np_name, 0)
    else:
        return 0


def login_pass_checker(login, file_path_for_login_checker, password=""):
    """
    Если принимает только логин и адрес файла, проверяет на наличие логина.
    Отдаёт 1 (True), если нашёл.
    Отдаёт 0 (False), если не нашёл.

    Если передать также пароль, то ищет пароль в строке с найденым логином и сравнивает с переданым паролем
    Отдаёт список ("логин", "пароль", "имя", "счёт"), если соответствует.
    Отдаёт 0 (False), если не соответствует.

    :param login:
    :param file_path_for_login_checker:
    :param password:
    :return:
    """
    with open(file_path_for_login_checker, "r", encoding="utf-8") as only_login_pass_file:
        for line in only_login_pass_file.readlines():
            if re.findall(r"^\w+", line)[0] == login:
                # Проверка пароля, если передали функции пароль
                if password:
                    if line.split(":")[1] == password:
                        return line.split(":")
                    else:
                        return 0
                return 1
        return 0

# TODO Когда будет вводиться счётчик, делать так: искать строчку по логину, на найденой строчке искать цифры счёта
#  и менять их через .replace(old_counter, new_counter) или найти способ как заменить текст в файле




#  Правила введения аргументов:
#  python FINAL_igra_Ugaday_chislo.py -dev_mode -123
#
#  -dev_mode (по умолчанию на задан) - Активировать режим разработчика.
#  (При выборе сложности будет показан ответ и диапазон)
#
#  -123 (по умолчанию 3) - Количество попыток.

# Введём общий счётчик попыток на будущее
wins_counter = 1

# Проверка на введение специальных ключей в аргументах к запуску игры через cmd
if len(sys.argv) > 1:
    if sys.argv[1] == "-dev_mode":
        dev_mode = True

    if len(sys.argv) > 2:
        argv_total_trys = int(sys.argv[2][1:])

# Модуль Логина/Регистрации
active_user = login_signup_asking()

print(f"active_user = {active_user}\n")

# Приветствие и предложение вывести правила (или продолжить на любой ввод)
print(f"""
=========================================================

          Добро пожаловать в Угадай Число, {active_user[2]}!

Чтобы прочесть правила, введите [Правила] или [0]
Чтобы сразу приступить к игре, нажмите [Enter]

=========================================================
""")

# Проверяем ответ по вопросу о правилах и выводим (или просто пропускаем)
starter_ques = input("Вводите: ")
if gtn.checking_ques(starter_ques):
    print("""
==============================================================

                      Правила игры
Нужно угадать случайное число. На это вам даётся 3 попытки.
Вам предложат выбрать сложность, их 3:

[1] - Легко. Случайное число в диапазоне от 1 до 5.
Проще простого!
[2] - Средне. Случайное число в диапазоне от 1 до 10.
Не так то просто...
[3] - Трудно. Случайное число в диапазоне от 1 до 25.
Настоящий вызов вашей удаче!""")  # Сообщение "Правила игры"
    input("""
Для продолжения нажмите [Enter]

==============================================================""")  # Продолжение на Enter

# Цикл даёт возможность перезапустить игру
while True:
    while True:
        difficulty = input("""
        
================================

        Введите сложность
        
[1] - от 1 до 5.
[2] - от 1 до 10.
[3] - от 1 до 25.

[0] - Правила

================================
        
        """)  # Вводим сложность 1 2 3

    # Если в выборе сложности 0, то показываем правила и спрашиваем о выборе сложности снова
        if gtn.checking_ques(difficulty):
            print("""
==============================================================

                      Правила игры
Нужно угадать случайное число. На это вам даётся 3 попытки.
Вам предложат выбрать сложность, их 3:

[1] - Легко. Случайное число в диапазоне от 1 до 5.
Проще простого!
[2] - Средне. Случайное число в диапазоне от 1 до 10.
Не так то просто...
[3] - Трудно. Случайное число в диапазоне от 1 до 25.
Настоящий вызов вашей удаче!""")  # Сообщение "Правила игры"
            input("""
Для продолжения нажмите [Enter]
        
==============================================================""")  # Продолжение на Enter
        elif gtn.checking_difficulty(difficulty):  #   Проверяем выбор сложности и продолжаем
            break

    number = gtn.checking_difficulty(difficulty)

    if "dev_mode" in globals():
        print(number)

    # Количество попыток (с возможностью регулирования через argv)
    if "argv_total_trys" in globals():
        total_trys = argv_total_trys
    else:
        total_trys = 3

    trys = total_trys  # Переменная для цикла

    while trys > 0:
        while True:  # Проверяем ответ на то, число ли он
            answer = input("\nВведите число: ")

            # В number[a, b, c] - a: сгенерированное ранд число, b: число для генерации ОТ, c: число ДО (включительно)

            if answer.isdigit() and number[1] <= int(answer) <= number[2]:
                # Правильный ввод получен
                answer = int(answer)
                break
            elif not answer.isdigit():
                print("То, что Вы ввели, не является целым числом.")
            else:
                print(f"Ваше число не в диапазоне,\nзаданном выбранным уровнем сложности! \
(От {number[1]} до {number[2]})")

        if answer == number[0]:
            # Сообщение "Победа!"
            print(f"""
==========================================

               Победа!
               
Задуманное число действительно было {number[0]}.
Тебе удалось с {(total_trys + 1) - trys} попытки!

==========================================""")
            input("""
            Для продолжения нажмите [Enter]
            """)  # Продолжение на Enter
            break
        elif answer < number[0]:
            print('Нет, загаданное число больше вашего.')
            trys -= 1
            print(f"Осталось {trys} попытки!")
        else:
            print('Нет, загаданное число меньше вашего.')
            trys -= 1
            print(f"Осталось {trys} попытки!")
    else:
        print(f"""
Больше попыток не осталось...
Число, которое было задумано: {number[0]}

В этот раз не удалось – получится в следующий!
""")  # Сообщение "Больше попыток не осталось"
        input("""
Для продолжения нажмите [Enter]
""")  # Продолжение на Enter


# Цикл для повтора вопроса о продолжении после Автор
    while True:
        start_again = input(f"""
===============================================

Попробовать сыграть ещё раз? :)
Общее количество побед подряд: {wins_counter}

[1] - Да
[0] - Нет

===============================================""")  # Сообщение "Попробовать еще раз? 1:продолжить, 0:нет"
        if start_again == "Автор":
            print("""
            ***********************************************
            ***********************************************
            ***                                         ***
            ***    Есть такой ( ^ ^)/                   ***
            ***                                         ***
            ***    Над программой работал я, Михаил!    ***
            ***                                         ***
            ***********************************************
            ***********************************************
            """)  # Авторство
            input("""
Для продолжения нажмите [Enter]
""")  # Продолжение на Enter

        if start_again == "1":
            break

    wins_counter += 1

    if start_again == "0":
        break

print("""

Хорошего дня!

""")

# TODO Прикрутить возможность создавать "аккаунт" с логин-паролем
# TODO Записывать логины в обычный txt, а пароли в отдельный txt и в зашифрованном виде.
# TODO Для каждого личного кабинета прикрутить возможность ввести своё имя \
#  и при логине в систему будет выходить Привет, Имя! (с возможностью в дальнейшем добвлять и другую информацию)