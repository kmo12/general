import string

def text_cleaning(text):
    """
    Функция получает текст, выводит текст без знаков препинания (оставляя дефис) и без цифр
    :param text:
    :return text:
    """
    text = str(text)

    # Текст в нижний регистр
    text = text.lower()

    # Убираем всю пунктуацию и дополнительно знак тирэ (дефис оставляем)
    for punc_char in string.punctuation:
        if punc_char == "-":
            continue
        text = text.replace(punc_char, "")
    text = text.replace("—", "")

    # Убираем все цифры
    # Модуль translate берёт таблицу и меняет все символы в тексте, в соответсвии с ней
    # Модуль maketrans создаёт таблицу (третьим параметром устанавливается str, каждый символ которого будет переведён)
    # с помощью translate в None (=> удалён)
    text = text.translate(text.maketrans("", "", string.digits))

    # Специфика вывода строк через readlines
    text = text.replace("\n", "")

    # Убираем двойные пробелы для простоты работы далее
    text = text.replace("  ", " ")

    return text


def read_file(read_name="R:\\python_module6_practicum3\\data.txt"):
    general_words_list = []

    with open(read_name, "r+", encoding="utf-8") as file:
        # Работаем с каждой отдельной строкой
        for line in file.readlines():
            # У каждой отдельной строки проходимся по словам и добавляем каждое в общий список
            # (каждую строку перед этим прогоняем через очиститель и разделяем на слова с помощью split)
            for word in text_cleaning(line).split(" "):
                general_words_list.append(word)

    # Оставляем уникальные слова
    general_words_list = set(general_words_list)
    general_words_list = list(general_words_list)

    return general_words_list


def save_file(words_list, save_name="R:\\python_module6_practicum3\\count.txt"):

    with open(save_name, "w", encoding="utf-8") as file:
        file.write("Количество уникальных слов: " + str(len(sorted(words_list))))
        file.write("\n======================")
        for word in sorted(words_list):
            file.write("\n" + word)


save_file(read_file())