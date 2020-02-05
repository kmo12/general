spisok = ['1', '2', '3']

print("""
Список команд для управления списком:
now - Узнать состояния списка сейчас
add - Добавить значение в список
del - Удалить введённый числом элемент
help - Список команд
exit - Выйти из программы
""")

while True:
    keyword = input("\n")

    if keyword.startswith("now"):
        print(spisok)

    elif keyword.startswith("add"):
        spisok.append(keyword[4:])

    elif keyword.startswith("del"):
        del spisok[int(keyword[4:])]

    elif keyword[0:4] == "help":
        print("""
Список команд для управления списком:
now - Узнать состояния списка сейчас
add - Добавить значение в список
del - Удалить введённый числом элемент
exit - Выйти из программы
""")

    elif keyword == "exit":
        print("Хорошего дня.")
        break

    else:
        print("Ошибочная команда")